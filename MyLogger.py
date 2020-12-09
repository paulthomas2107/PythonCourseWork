import logging
import logging.config

logging.config.fileConfig('logging.conf')

logger = logging.getLogger('simpleExample')
logger.debug('Hi, another debug message')

"""
logger = logging.getLogger(__name__)
# logger.info('Hello from MyLogger....')
# Create handler
stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler('file.log')

# Level and Format
stream_handler.setLevel(logging.WARNING)
file_handler.setLevel(logging.ERROR)

formatter = logging.Formatter('%(name)s - %(levelname)s- %(message)s')
stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

# Test it
logger.warning('This is a warning est')
logger.error('This is an error test')
"""
