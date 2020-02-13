
import os, sys
sys.path.insert(0, '/var/www/u0786583/data/www/blask.ru/task')
sys.path.insert(1, '/var/www/u0786583/data/lezettyVirtual/lib/python3.7/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'task.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()