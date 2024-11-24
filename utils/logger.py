import logging

class Logger:
    """Singleton class for setting up a logger."""
    _logger = None  # Holds the singleton logger instance

    @staticmethod
    def get_logger(log_file='project.log', level=logging.INFO):
        """
        Get the logger instance. Sets up the logger if it hasn't been initialized.
        Args:
            log_file (str): Path to the log file.
            level (int): Logging level (e.g., logging.INFO, logging. DEBUG).
        Returns:
            logging.Logger: Configured logger instance.
        """
        if Logger._logger is None:
            Logger._logger = logging.getLogger('ProjectLogger')
            Logger._logger.setLevel(level)

            # Create handlers
            file_handler = logging.FileHandler(log_file)
            console_handler = logging.StreamHandler()

            # Create formatters and add to handlers
            formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
            file_handler.setFormatter(formatter)
            console_handler.setFormatter(formatter)

            # Add handlers to the logger
            Logger._logger.addHandler(file_handler)
            Logger._logger.addHandler(console_handler)

        return Logger._logger
