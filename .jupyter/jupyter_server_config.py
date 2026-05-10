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
            '--homepath', GRAFANA_PATH
        ],
        'port': GRAFANA_PORT,
        'timeout': 30,        
        'environment': {
            'GF_SERVER_HTTP_PORT': str(GRAFANA_PORT),
            'GF_SERVER_ROOT_URL': '{base_url}grafana/',
            'GF_SERVER_SERVE_FROM_SUB_PATH': 'true',
            'GF_SERVER_ENFORCE_DOMAIN': 'false',
            'GF_SECURITY_ALLOW_EMBEDDING': 'true'
        },
        
        # Garante que o Jupyter não tente adivinhar e duplicar os redirecionamentos
        'absolute_url': True,
        
        'launcher_entry': {
            'title': 'Grafana',
            'icon_path': os.path.join(GRAFANA_PATH, 'public/img/fav32.png') if GRAFANA_PATH else None,
        }
    }
}