import paho.mqtt.client as paho
import datetime
from threading import Thread
import ipywidgets as widgets
import time
import random 
import json
from dateutil import tz                                    
from threading import Thread
from influxdb_client_3 import InfluxDBClient3, Point, WriteOptions
import asyncio  
import queue



class IoTSensorConsumer():
    
    def __init__(self, broker, port, topic):
        self.topic = topic
        self.broker = broker
        self.port = port
        
        # Fila thread-safe para enviar dados da Thread do MQTT para a Thread da UI
        self.ui_queue = queue.Queue()
        
        self.client = paho.Client(paho.CallbackAPIVersion.VERSION2)
        self.client.on_message = self.on_message
        self.client.on_connect = self.on_connect
        self.client.connect(self.broker, self.port)
        
    def on_connect(self, client, userdata, flags, reason_code, properties):
        if reason_code == 0:
            self.client.subscribe(self.topic)
            print(f"Inscrito com sucesso em {self.topic}")
        else:
            print(f"Falha de conexão ao broker MQTT: {reason_code}")
            
            
    def on_message(self, client, userdata, msg):
        try:
            payload_str = str(msg.payload.decode("utf-8"))
            payload = json.loads(payload_str)
            
            self.ui_queue.put(payload)
                        
            point = Point("cliente_a").tag("sensor_id", payload['name'])\
                                      .field(payload['body']['dimension'],\
                                             float("{:.2f}".format(payload['body']['value'])))
            self.influx_client.write(point)        
            
        except Exception as e:
            print(f"Erro no processamento MQTT: {e}")

    async def _ui_update_loop(self):
        while True:
            try:
                # Tenta pegar um dado da fila sem travar a thread (non-blocking)
                payload = self.ui_queue.get_nowait()
                
                # Atualiza os widgets com segurança total na thread principal
                novo_valor = float("{:.2f}".format(payload['body']['value']))
                self.widget.value = novo_valor
                self.widget.description = "{} {}".format(payload['source'], payload['name'])
                self.widget_label.value = "{0}: {1:.2f} {2}".format(
                    payload['body']['dimension'], 
                    payload['body']['value'], 
                    payload['body']['unity']
                )
                
                self.ui_queue.task_done()
            except queue.Empty:
                # Se a fila estiver vazia, aguarda um instante para não estressar a CPU
                await asyncio.sleep(0.1)
            except Exception as e:
                print(f"Erro ao atualizar UI: {e}")
                await asyncio.sleep(0.1)

    def start_consuming(self, widget, widget_label):
        self.widget = widget
        self.widget_label = widget_label
        self.influx_client = InfluxDBClient3(host="http://127.0.0.1:8181", database="exemplo_iot")
        
        # Dispara o loop do MQTT
        self.client.loop_start()
        
        # Cria uma tarefa de background no loop principal do Jupyter para atualizar a tela
        asyncio.create_task(self._ui_update_loop())





class IoT_mqtt_publisher:

    def __init__(self, broker, port):
        self.broker = broker
        self.port = port
        self.client = None
        self.connect()
        
    def connect(self):
        # self.client = paho.Client()
        self.client = paho.Client(paho.CallbackAPIVersion.VERSION2, "publisher{0}".format(random.randint(0,99999999)))

        if(not self.client.connect(self.broker, self.port)):                     #establish connection
            print("Connected.")        
        
    def publish(self, topic, payload):
        self.client.publish(topic,payload)  
        
                


class IoT_sensor(Thread):
    
    def __init__(self, name, dimension, unity, min_value, max_value, pooling_interval):
        Thread.__init__(self)        
        self.name = name
        self.dimension = dimension    
        self.unity = unity    
        self.max_value = max_value
        self.min_value = min_value    
        self.pooling_interval = pooling_interval
        self.publisher = None
        self.flag = True


    def connect(self, publisher):
        self.publisher = publisher
        self.start()

    def stop(self):
        self.flag = False
        
    def resume(self):
        self.flag = True
        self.run()
        
    def run(self):
        
        while self.flag:
            payload = {
                "source":"sensor",
                "name":self.name,
                "type":"reading",
                "body": {
                    "timestamp": datetime.datetime.utcnow().isoformat("T") + "Z",
                    "dimension": self.dimension,
                    "value": random.uniform(self.min_value,self.max_value),
                    "unity": self.unity                
                }

            }
            time.sleep(self.pooling_interval)
            self.publisher.publish( "sensor/{0}/{1}".format(self.name, self.dimension),
                                    json.dumps(payload))
