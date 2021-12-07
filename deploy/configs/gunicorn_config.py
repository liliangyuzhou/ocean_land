#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： liliang
# datetime： 2021/12/7 14:17 
# email： liang1.li@ximalaya.com

bind = '0.0.0.0:8000'
reload = True
pidfile = '/usr/src/app/logs/gunicorn.pid'
accesslog = '/usr/src/app/logs/gunicorn_acess.log'
errorlog = '/usr/src/app/logs/gunicorn_error.log'
