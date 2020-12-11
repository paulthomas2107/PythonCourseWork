# Logging techniques
import logging
import traceback
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler
import time

# Config logger
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s- %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

try:
    a = [1, 2, 3]
    val = a[100]
except:
    logging.error("The error is %s", traceback.format_exc())

print('=' * 50)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

""" handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5) """
handler = TimedRotatingFileHandler('timed_test.log', when='s', interval=5, backupCount=2)
logger.addHandler(handler)

for _ in range(6):
    logger.info('Hello Paul.....and world.')
    time.sleep(6)

print('=' * 50)