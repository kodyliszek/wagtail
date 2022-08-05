from .base import *

DEBUG = False

try:
    from .local import *
except ImportError:
    pass
print(os.environ)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['DBNAME'],
        'HOST': os.environ['DBHOST'],
        'USER': os.environ['DBUSER'],
        'PASSWORD': os.environ['DBPASSWORD']
    }
}