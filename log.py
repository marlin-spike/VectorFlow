import logging
import os
import colorlog

try:
    # Create a logger
    logger = colorlog.getLogger()
    logger.setLevel(logging.DEBUG)

    # Create a formatter
    formatter = colorlog.ColoredFormatter(
        '%(asctime)s - %(log_color)s%(levelname)s%(reset)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        log_colors={
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'red,bg_white',
        }
    )

    # Create a file handler with 'a' mode for appending
    file_handler = logging.FileHandler('data.log', mode='a')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    # Add the file handler to the logger
    logger.addHandler(file_handler)

    # Custom log messages
    logger.debug('This is a debug message')
    logger.info('This is an info message')
    logger.warning('This is a warning message')
    logger.error('This is an error message')
    logger.critical('This is a critical message')

except Exception as e:
    print("An error occurred:", e)

print("Current working directory:", os.getcwd())

