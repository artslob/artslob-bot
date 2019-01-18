from logging.config import dictConfig

from config import LOG_BASE

LOGGING = {
    'version': 1,
    'root': {
        'level': 'DEBUG',
        'handlers': ['root'],
    },
    'loggers': {
        'webhook': {
            'level': 'DEBUG',
            'handlers': ['webhook', 'exceptions', 'console'],
            'propagate': False,
        },
    },
    'handlers': {
        'root': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'defaultFormatter',
            'filename': str(LOG_BASE / 'root.log'),
        },
        'webhook': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'defaultFormatter',
            'filename': str(LOG_BASE / 'webhook.log'),
        },
        'exceptions': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'formatter': 'defaultFormatter',
            'filename': str(LOG_BASE / 'exceptions.log'),
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'defaultFormatter',
        },
    },
    'formatters': {
        'defaultFormatter': {
            'class': 'logging.Formatter',
            'format': '[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
            'datefmt': '%d/%b/%Y %H:%M:%S',
        },
    },
}


def init_log():
    dictConfig(LOGGING)
