import logging
from logging__.foo import foo2

if __name__ == '__main__':
    logging.basicConfig(filename='some_log.log',
                        filemode="w",
                        format='%(levelname)s\t%(message)s\t%(asctime)s\t%(pathname)s\tLine:%(lineno)d',
                        level=logging.DEBUG)
    sh = logging.StreamHandler()
    # use add addHandler to enable the logging print in the console.
    logging.getLogger('').addHandler(sh)
    logging.debug('Debug message')
    logging.info('Info message')
    logging.warning('Warning message')
    foo2()
