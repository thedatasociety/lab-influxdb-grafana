import os

# Se a variável 'GRAFANA_PORT_ENV' existir, usa ela. Se não, usa 3000 como padrão.
GRAFANA_PORT = int(os.environ.get('GRAFANA_PORT_ENV', 3000))

# Buscando o caminho do Grafana de uma variável de ambiente, com um fallback local
GRAFANA_PATH = os.environ.get('GRAFANA_HOME')

c.ServerProxy.servers = {
    'grafana': {
        'command': [
            'grafana',
            'server',            
            '--homepath', GRAFANA_PATH,
            '--config', '', 
            f'cfg:default.server.http_port={GRAFANA_PORT}',
            'cfg:default.server.root_url={base_url}grafana/',
            'cfg:default.server.serve_from_sub_path=true',
        ],
        'port': GRAFANA_PORT,
        'timeout': 30,
        'launcher_entry': {
            'title': 'Grafana',
            # Usando a variável de caminho para o ícone também
            'icon_path': os.path.join(GRAFANA_PATH, 'public/img/fav32.png'),
        }
    }
}