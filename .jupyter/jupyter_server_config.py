import os
import random

# --- Grafana Configs ---
GRAFANA_PORT = int(os.environ.get('GRAFANA_PORT_ENV', 3000))
GRAFANA_PATH = os.environ.get('GRAFANA_HOME')
HOME = os.environ.get('HOME')

GRAFANA_PROVISIONING_PATH = f'{HOME}/resources/configs/grafana'
GRAFANA_PLUGINS_PATH      = f'{HOME}/resources/configs/grafana/plugins'
os.makedirs(GRAFANA_PLUGINS_PATH, exist_ok=True)

MONGO_ZIP_URL = "https://github.com/haohanyang/mongodb-datasource/releases/download/v0.5.0/haohanyang-mongodb-datasource-0.5.0.zip"

# --- Mongo Express Configs ---
MONGO_EXPRESS_PORT = int(os.environ.get('MONGO_EXPRESS_PORT_ENV', 7777))
# Change this if your MongoDB is hosted elsewhere or requires credentials
MONGODB_URL = os.environ.get('MONGO_URL', 'mongodb://localhost:27017/') 
MONGO_EXPRESS_HOME = os.environ.get('MONGO_EXPRESS_HOME')


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
            'GF_SECURITY_ALLOW_EMBEDDING': 'true',
            'GF_USERS_ALLOW_PASSWORD_CHANGE': 'true',
            'GF_SECURITY_DISABLE_INITIAL_ADMIN_PASSWORD_CHANGE': 'true',
            'GF_PATHS_PROVISIONING': GRAFANA_PROVISIONING_PATH,
            'GF_LOG_LEVEL': 'error',
            'GF_PLUGINS_ALLOW_UNSIGNED': 'haohanyang-mongodb-datasource',
            'GF_PLUGINS_ALLOW_LOADING_UNSIGNED_PLUGINS':  'haohanyang-mongodb-datasource',
            'GF_PATHS_PLUGINS': GRAFANA_PLUGINS_PATH,            
            'GF_INSTALL_PLUGINS': f"{MONGO_ZIP_URL};haohanyang-mongodb-datasource",            
        },
        'absolute_url': True,
        'launcher_entry': {
            'title': 'Grafana',
            'icon_path': os.path.join(GRAFANA_PATH, 'public/img/fav32.png') if GRAFANA_PATH else None,
        }
    },
    
    'mongo-express': {
        'command': [
                    'bash', '-c', f'cd "{MONGO_EXPRESS_HOME}" && node app.js --admin'
        ],
        'port': MONGO_EXPRESS_PORT,
        'timeout': 60,
        'environment': {
            'PORT': str(MONGO_EXPRESS_PORT),
            'ME_CONFIG_MONGODB_URL': MONGODB_URL,
            'ME_CONFIG_SITE_BASEURL': '{base_url}mongo-express/',
            'ME_CONFIG_BASICAUTH': 'false',
            'ME_CONFIG_BASICAUTH_ENABLED': 'false',
            'ME_CONFIG_BASICAUTH_USERNAME': '',
            'ME_CONFIG_BASICAUTH_PASSWORD': '',
            'VCAP_APP_HOST': '127.0.0.1',            
            'ME_CONFIG_MONGODB_ENABLE_ADMIN': 'true',
            'ME_CONFIG_SITE_COOKIESECRET': f"{random.randint(9999, 99999999)}",
            'ME_CONFIG_SITE_SESSIONSECRET': f"{random.randint(9999, 99999999)}",
        },
        'absolute_url': True,
        'launcher_entry': {
            'title': 'Mongo Express',
            'icon_path': os.path.join(MONGO_EXPRESS_HOME, 'public/images/mongo-express-logo.png') if GRAFANA_PATH else None
        }
    }
}