import logging
import time

class AppLogging:
    def __init__(self):
        logging.basicConfig(filename="newfile.log",
                            format='%(asctime)-5s %(levelname)-5s %(message)s',
                            filemode='a')

def warn_function(message):
        logger = logging.getLogger()
        logger.setLevel(logging.WARN)
        logger.warning(message)
        print(" warn called")
def error_function(message):
        logger = logging.getLogger()
        logger.setLevel(logging.ERROR)
        logger.error(message)
        print(" error called")
def info_function(message):
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        logger.info(message)
        print(" info called")
def debug_function(message):
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        logger.debug(message)
        print(" debug called")
"""def main():
    obj = AppLogging()
    obj.debug_function()
    obj.error_function()
    obj.info_function()
    obj.warn_function()
***




if __name__ == '__main__':
    main() """



