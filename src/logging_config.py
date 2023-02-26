import logging
# Set up logger for INFO level
info_logger = logging.getLogger("info_logger")
info_logger.setLevel(logging.INFO)
info_formatter = logging.Formatter("\x1B[3m%(levelname)s: %(message)s\x1B[0m")
info_handler = logging.StreamHandler()
info_handler.setFormatter(info_formatter)
info_logger.addHandler(info_handler)

# Set up logger for ERROR level
error_logger = logging.getLogger("error_logger")
error_logger.setLevel(logging.ERROR)
error_formatter = logging.Formatter("\033[31m%(levelname)s: %(message)s\x1B[0m")
error_handler = logging.StreamHandler()
error_handler.setFormatter(error_formatter)
error_logger.addHandler(error_handler)

# Log messages
info_logger.info("This is an info message")
error_logger.error("This is an error message")