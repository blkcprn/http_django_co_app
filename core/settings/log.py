from .paths import LOG_DIR


LOG_MAX_BYTES = 1024 * 1024 * 10 # 10Mb
LOG_BACKUP_COUNT = 10

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{asctime}:{levelname}:{module}:{filename}:{lineno}:{message}",
            "datefmt": "%Y-%m-%d %H:%M:%S",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
        },
        "app": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": LOG_DIR / "app/app.log",
            "maxBytes": LOG_MAX_BYTES, 
            "backupCount": LOG_BACKUP_COUNT,
            "formatter": "verbose",
        },
        "auth": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": LOG_DIR / "auth/auth.log",
            "maxBytes": LOG_MAX_BYTES, 
            "backupCount": LOG_BACKUP_COUNT,
            "formatter": "verbose",
        },
        "admin": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": LOG_DIR / "admin/admin.log",
            "maxBytes": LOG_MAX_BYTES, 
            "backupCount": LOG_BACKUP_COUNT,
            "formatter": "verbose",
        },
    },
    "loggers": {
        "app": {
            "handlers": ["app", "console"],
            "level": "DEBUG",
        },
        "auth": {
            "handlers": ["auth", "console"],
            "level": "DEBUG",
        },
        "admin": {
            "handlers": ["admin", "console"],
            "level": "DEBUG",
        },
    },
}