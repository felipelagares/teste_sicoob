import logging
from pathlib import Path

# Cria a pasta de logs caso não exista
Path("logs").mkdir(exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.FileHandler("logs/execution.log", encoding="utf-8"),
        logging.StreamHandler()  # Também exibe no console
    ]
)

default_logger = logging.getLogger(__name__)