import logging.config

class Logger:
    def __init__(self, name):
        logging.basicConfig(level=logging.INFO, filename=r".//app//app.log", filemode='w', format='%(asctime)s - %(name)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
        self.logger = logging.getLogger(name)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self,message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)