#!/usr/bin/python

import sys
import logging
logging.basicConfig(stream=sys.stderr)

sys.path.append('/var/www/flask_dev')
#sys.path.insert(0, '/var/www/flask_dev')

from appneta import app as application

