"""
Centralized logging configuration for the Autonomous Research Agent.
"""

import logging


def setup_logger(name: str = "ARA") -> logging.Logger:
    """
    Create and configure a logger.

    Args:
        name: Name of the logger.

    Returns:
        Configured logger instance.
    """

    logger = logging.getLogger(name)

    if logger.hasHandlers(): # This check prevents duplicate log output.
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)

    return logger


logger = setup_logger()