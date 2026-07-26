from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    # class Config:
    #     env_file = ".env"
    model_config = SettingsConfigDict(
        env_file=".env",              # Load from a local .env file
        env_file_encoding="utf-8",    # Define file encoding
        # env_prefix="APP_",            # Look for APP_DATABASE_URL instead of DATABASE_URL
        case_sensitive=False         # Treat APP_DB and app_db identically
    )

settings = Settings()