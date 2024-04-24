import logging


class Format(logging.Formatter):
    grey = '\x1b[38;21m'
    yellow = '\x1b[33;21m'
    red = '\x1b[31;21m'
    bold_red = '\x1b[31;1m'
    reset = '\x1b[0m'

    log_format = '[%(asctime)s] %(levelname)s | %(message)s'

    FORMATS = {
        logging.DEBUG: grey + log_format + reset,
        logging.INFO: grey + log_format + reset,
        logging.WARNING: yellow + log_format + reset,
        logging.ERROR: red + log_format + reset,
        logging.CRITICAL: bold_red + log_format + reset
    }

    def format(self, record: logging.LogRecord) -> logging.LogRecord:
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


class Filter(logging.Filter):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.filter_items = [
            'GET /static/',
            '"GET /static/',
            'GET /favicon.ico',
            '"GET /favicon.ico',
            'Not Found: /static/',
            '"Not Found: /static/',
            'Not Found: /favicon.ico',
            '"Not Found: /favicon.ico',
            'GET /healthcheck/',
            '"GET /healthcheck/',
            'GET /admin/jsi18n/',
            '"GET /admin/jsi18n/',
        ]

    def filter(self, record: logging.LogRecord) -> bool:
        message = record.getMessage()
        return all([
            not message.startswith(filter_item)
            for filter_item in self.filter_items
        ]) and ('svg' not in message)


def get_logging(filter: logging.Filter) -> dict:
    return {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'verbose': {
                '()': Format,
                'format': '[{asctime}] {levelname} | ({module}) {message}',
                'style': '{',
            },
        },
        'filters': {
            'custom_filter': {
                '()': filter,
            }
        },
        'disable_existing_loggers': False,
        'handlers': {
            'console': {
                'level': 'INFO',
                'class': 'logging.StreamHandler',
                'filters': ['custom_filter'],
                'formatter': 'verbose'
            },
        },
        'loggers': {
            'django': {
                'level': 'INFO',
                'handlers': ['console'],
            }
        },
    }
