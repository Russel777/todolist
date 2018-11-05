from .base import *

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'todolist',
        'USER': 'rus',  # ENTER USERNAME
        'PASSWORD': 'hekbn',  # ENTER PASS
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

TIME_ZONE = 'Asia/Novosibirsk'
