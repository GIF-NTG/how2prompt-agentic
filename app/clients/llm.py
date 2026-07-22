import logging
import litellm
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
from app.core.config import settings

logger = logging.getLogger(__name__)

class LLMClient:
    def __init__(self) -> None:
        # LiteLLM automatically resolves API keys from env: ANTHROPIC_API_KEY, OPENAI_API_KEY, etc.
        pass

    @retry(
        reraise=True,
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=1, max=5),
        retry=retry_if_exception_type((
            litellm.exceptions.Timeout,
            litellm.exceptions.APIConnectionError,
            litellm.exceptions.ContextWindowExceededError
        ))
    )
    async def completion(self, messages: list[dict], response_format=None) -> dict:
        """
        Wrapper to perform completion using LiteLLM with built-in retry handling.
        """
        logger.info(f"Initiating completion with model: {settings.default_llm_model}")
        try:
            # Call LiteLLM async completion
            response = await litellm.acompletion(
                model=settings.default_llm_model,
                messages=messages,
                response_format=response_format,
            )
            return response
        except litellm.exceptions.APIError as e:
            logger.error(f"LiteLLM Provider error occurred: {str(e)}")
            # Propagate up to be caught by services or routers
            raise e
        except Exception as e:
            logger.error(f"Unexpected completion error: {str(e)}")
            raise e
