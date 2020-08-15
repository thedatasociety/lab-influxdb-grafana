from IPython.core.display import HTML 
import os


def list_urls(binderhub_urls):
    url_message='<a href="http://{0}{1}{2}" target="_blank"> http://{0}{1}{2}</a> <br/>'
    print("\nO Grafana está disponível em alguma das URLs abaixo, dependendo do servidor escolhido: \n")
    for url in binderhub_urls:
        display(HTML(url_message.format(url,os.getenv('JUPYTERHUB_SERVICE_PREFIX', "" ),"/proxy/3000")))

    display(HTML('<b>User</b>: admin  | <b>Password:</b> admin'))