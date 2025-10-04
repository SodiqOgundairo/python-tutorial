# 5 security levels of logging


# DEBUG - to debug, test, troubleshoot for developers to know what went wrong or anything else

# INFO - informational messages that doesn't require attention, can be printed or not

# WARNING - indicating nothing bad happened yet, but telling you something miht happen, e.g. low storage space left

# ERROR - something went wrong and while the system is still running but can't perform the expected task

# CRITICAL - when a part of the system breaks down and needs immediate attention

import logging

# logging has security levels so the level you set it at determines what get logged e.g

# logging.basicConfig(level=logging.DEBUG)
#
#
# logging.info("You've got 20 emails in your inbox!")
# logging.critical("All components failed!")


# above are in-built loggers
# let's create custom logs

logger = logging.getLogger('Yemi the Logger')
# logger.info('The best logger was just created!')
# logger.critical('Your Figma Account has been disabled lol')
# logger.log(logging.ERROR, 'An Error occured!')

logger.setLevel(logging.DEBUG)
# sending the logs to a file

handler = logging.FileHandler('logs.log')
# you don't want to send in debugging messages to the user so just do this below
handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(levelname)s - %(asctime)s: %(message)s")
handler.setFormatter(formatter)

logger.addHandler(handler)

# logger.debug('This is a debug message!')
# logger.info('This is a important info!')
