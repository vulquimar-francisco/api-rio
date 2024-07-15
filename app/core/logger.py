import logging
import os

# Configurações de log
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_FILE = os.getenv("LOG_FILE")

# Configurando o logger
logger = logging.getLogger(__name__)
logger.setLevel(LOG_LEVEL)

# Formatação do log
formatter = logging.Formatter(LOG_FORMAT)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# File handler, se especificado
if LOG_FILE:
    file_handler = logging.FileHandler(LOG_FILE)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

logger.info(f"Logger inicializado com nível {LOG_LEVEL}")
