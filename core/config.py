from pydantic import BaseSettings


class Settings(BaseSettings):
    ...


config = Settings(".env")