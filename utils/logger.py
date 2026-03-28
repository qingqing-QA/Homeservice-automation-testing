import logging
import os
from datetime import datetime

def get_logger(name="automation"):
    """
    Create and return a configured logger
    """

    # Creat log
    log_dir = "logs"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # 
    log_file = os.path.join(
        log_dir, f"test_{datetime.now().strftime('%Y-%m-%d')}.log"
    )

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # 
    if logger.hasHandlers():
        return logger

    # Console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Output
    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setLevel(logging.INFO)

    # 
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # Add handler
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger
