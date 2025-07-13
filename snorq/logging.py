import logging
import colorlog


def get_logger() -> logging.Logger:
    """
    Returns a logger with color formatting
    :return:
    """

    logger = logging.getLogger("Sniffy.Core")
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = colorlog.ColoredFormatter(
            "[%(asctime)s %(name)s]: %(message)s",
            datefmt="%H:%M:%S",
            log_colors={
                "DEBUG": "green",
                "INFO": "yellow",
                "WARNING": "red",
                "ERROR": "red",
                "CRITICAL": "bold_red",
            }
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.propagate = False
    return logger
