import enum

import pydantic


class AppEnv(enum.Enum):
    PROD = "prod"
    DEV = "dev"


class BaseAppSettings(pydantic.BaseSettings):
    APP_ENV: AppEnv = AppEnv.PROD

    class Config(pydantic.BaseSettings.Config):
        env_file = ".env"
