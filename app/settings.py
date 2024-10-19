import os
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # NOTE: .envファイルや環境変数が同名の変数にセットされる
    TITLE: str = "FastAPI Sample"
    ENV: str = ""
    DEBUG: bool = False
    VERSION: str = "0.0.1"
    CORS_ORIGINS: list[str] = [
        "http://localhost:8000",
        "http://127.0.0.1:8000",
        "http://localhost:3000",
        "http://localhost:3333",
    ]
    BASE_DIR_PATH: str = str(Path(__file__).parent.parent.absolute())
    ROOT_DIR_PATH: str = str(Path(__file__).parent.parent.parent.absolute())

    # DB設定
    DB_HOST: str
    DB_PORT: str
    DB_NAME: str
    DB_USER_NAME: str
    DB_PASSWORD: str

    SECRET_KEY: str = "secret"
    LOGGER_CONFIG_PATH: str = os.path.join(BASE_DIR_PATH, "logger_config.yaml")

    def get_database_url(self, is_async: bool = False) -> str:
        """DB接続用のURLを取得する"""
        if is_async:
            return f"postgresql+asyncpg://{self.DB_USER_NAME}:{self.DB_PASSWORD}@{self.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
        else:
            return f"postgresql://{self.DB_USER_NAME}:{self.DB_PASSWORD}@{self.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"

    model_config = SettingsConfigDict(env_file=".env")

    def get_app_title(self, app_name: str) -> str:
        return f"[{self.ENV}]{self.TITLE}({app_name=})"


settings = Settings()  # type: ignore
