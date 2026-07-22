from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    # API credentials and LLM configuration
    anthropic_api_key: str | None = None
    openai_api_key: str | None = None
    default_llm_model: str = "claude-3-5-sonnet-20240620"

    # Retry mechanism parameters
    max_retries: int = 3
    retry_min_backoff_seconds: float = 1.0
    retry_max_backoff_seconds: float = 5.0

    # Server configuration
    port: int = 8000
    host: str = "0.0.0.0"
    log_level: str = "info"

settings = Settings()
