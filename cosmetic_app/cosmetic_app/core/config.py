from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_url: str = "postgresql+asyncpg://postgres:qwerty@localhost:5432/cosmetic"
    api_v1_prefix: str = "/api/v1"
    db_username: str = "postgres"
    db_password: str = "qwerty"
    db_name: str = "cosmetic"
    db_echo: bool = True


settings = Settings()
