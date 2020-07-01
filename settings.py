import os

# import sentry_sdk
# from db.enums import CacheTable
from dotenv import load_dotenv

# from sentry_sdk.integrations.redis import RedisIntegration

load_dotenv()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

API_SECRET = os.getenv('API_SECRET')
ADMIN_SECRET = os.getenv('ADMIN_SECRET')

# sentry_sdk.init(
#     dsn=os.getenv('SENTRY_DSN'),
#     environment=os.getenv('ENVIRONMENT', 'development'),
#     integrations=[RedisIntegration()]
# )
DEBUG = os.getenv('DEBUG') == 'True'
PROJECT_CODE = 'REWARD'

DB_HOST = os.getenv('DB_HOST', '127.0.0.1')
DB_PORT = os.getenv('DB_PORT', 3306)
DB_USER = os.getenv('DB_USER', 'root')
DB_NAME = os.getenv('DB_NAME', 'tortoise')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'root')

TORTOISE_ORM = {
    'connections': {
        'default': {
            'engine': 'tortoise.backends.mysql',
            'credentials': {
                'host': DB_HOST,
                'port': DB_PORT,
                'user': DB_USER,
                'password': DB_PASSWORD,
                'database': DB_NAME,
                'echo': os.getenv('DB_ECHO') == 'True',
                'maxsize': 10,
            }
        },
    },
    'apps': {
        'models': {
            'models': ['models'],
            'default_connection': 'default',
        },
    },
}

REDIS_HOST = os.getenv('REDIS_HOST', '127.0.0.1')
REDIS_PORT = os.getenv('REDIS_PORT', 6379)
REDIS_PASSWORD = os.getenv('REDIS_PASSWORD')

REDIS = {
    'host': REDIS_HOST,
    'port': REDIS_PORT,
    'password': REDIS_PASSWORD,
    'db': 2,
    'encoding': 'utf-8'
}

ARQ = {
    'host': REDIS_HOST,
    'port': REDIS_PORT,
    'password': REDIS_PASSWORD,
    'database': 1,
}
