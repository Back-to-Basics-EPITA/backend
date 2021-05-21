# import default settings
from .settings import *

# enable debug
DEBUG = True
ALLOWED_HOSTS = []
DATABASES["default"]["NAME"] = DATABASES_DIR / 'db.dev.sqlite3'

print("\033[91;1;5m\n\n\n"
  "***************************************\n"
  "**                                   **\n"
  "**     WARNING RUN IN DEBUG MODE     **\n"
  "**                                   **\n"
  "***************************************\n"
  "\n\n\n\033[0m"
)
