import logging
import sys
from app.core.config import settings

def setup_logging() -> None:
    # Setup standard python logging
    log_level = getattr(logging, settings.log_level.upper(), logging.INFO)

    # In local development we want clean text, in production we can configure JSON formatted logs
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )

    # Suppress verbose logs from third party providers (like LiteLLM or HTTPX) if needed
    logging.getLogger("openai").setLevel(logging.WARNING)
    logging.getLogger("httpcore").setLevel(logging.WARNING)
    logging.getLogger("httpx").setLevel(logging.WARNING)
