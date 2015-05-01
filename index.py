#-*- coding:utf-8 -*-

import os
#安装我们的模块
os.environ['DJANGO_SETTINGS_MODULE'] = 'yellowcong.settings'

from django.core.wsgi import get_wsgi_application
from bae.core.wsgi import WSGIApplication
application = WSGIApplication(get_wsgi_application())
