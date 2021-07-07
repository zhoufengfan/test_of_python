import logging
# from logging__.foo import foo2
from rich.logging import RichHandler

if __name__ == '__main__':
    use_rich_handler = True
    logging.basicConfig(filename=r'D:\some_log.log',
                        filemode="w",
                        format='%(levelname)s\t%(message)s\t%(asctime)s\t%(pathname)s\tLine:%(lineno)d',
                        level=logging.DEBUG)
    if use_rich_handler:
        sh = RichHandler()
    else:
        sh = logging.StreamHandler()
    # use add addHandler to enable the logging print in the console.
    logging.getLogger('').addHandler(sh)
    logging.debug("[bold red blink]debug message[/]", extra={"markup": True})
    logging.info('Info message')
    logging.warning('Warning message')
    try:
        raise RuntimeError("sdfsa")
    except Exception as exception:
        logging.exception(exception)
