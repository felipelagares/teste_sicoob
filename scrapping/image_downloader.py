import logging
from pathlib import Path
from urllib.parse import urlparse

import requests


logger = logging.getLogger(__name__)


def download_image(image_url: str, book_name: str, output_dir: str = "images") -> str | None:
    """
    Faz o download da imagem de um livro.

    Args:
        image_url: URL da imagem.
        book_name: Nome do livro (utilizado no nome do arquivo).
        output_dir: Pasta onde a imagem será salva.

    Returns:
        Caminho da imagem salva ou None caso ocorra erro.
    """

    try:
        Path(output_dir).mkdir(parents=True, exist_ok=True)

        # Remove caracteres inválidos do nome do arquivo
        safe_name = "".join(
            c if c.isalnum() or c in (" ", "-", "_") else "_"
            for c in book_name
        ).strip()

        extension = Path(urlparse(image_url).path).suffix or ".jpg"

        file_path = Path(output_dir) / f"{safe_name}{extension}"

        response = requests.get(image_url, timeout=15)
        response.raise_for_status()

        with open(file_path, "wb") as image_file:
            image_file.write(response.content)

        logger.info(f"Imagem salva: {file_path}")

        return str(file_path)

    except Exception as e:
        logger.exception(f"Erro ao baixar imagem '{book_name}': {e}")
        return None