from pathlib import Path

# Build paths inside the project like this: BASE_DIR / "subdir".
BASE_DIR = Path(__file__).resolve().parent.parent.parent

TEMPLATES_DIR = BASE_DIR / "templates"

CACHE_DIR = BASE_DIR / "cache"

LOCALE_DIR = BASE_DIR / "locale"

LOG_DIR = BASE_DIR / "log"

STATIC_DIR = BASE_DIR / "static"

MEDIA_DIR = BASE_DIR / "media/"

TMP_DIR = BASE_DIR / "tmp"

URL_STATIC = "static/"

URL_MEDIA = "/media/"