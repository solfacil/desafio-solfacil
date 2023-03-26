import os
from pathlib import Path

# --------------------------------------------------

__version__ = "0.1.0.1"

BASE_DIR = Path(__file__).parent

# configfile = ConfigFile(BASE_DIR, print_when_create=False)

# --------------------------------------------------

db_infos = {
    'drivername': os.environ.get('DB_DRIVER_NAME', None),
    'username': os.environ.get('DB_USERNAME', None),
    'password': os.environ.get('DB_PASSWORD', None),
    'host': os.environ.get('DB_HOST', None),
    'database': os.environ.get('DB_DATABASE', None),
}
EMAIL_ENABLED = bool(int(os.environ.get('EMAIL_ENABLED', '0')))
email_infos = {
    'username': os.environ.get('EMAIL_USERNAME', None),
    'password': os.environ.get('EMAIL_PASSWORD', None),
    'smtp_host': os.environ.get('EMAIL_SMTP_HOST', None),
    'smtp_port': os.environ.get('EMAIL_SMTP_PORT', None)
}
