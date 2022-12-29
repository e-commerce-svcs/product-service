from app.core.settings.app import AppSettings


class DevAppSettings(AppSettings):
    DEBUG: bool = True

    class Config(AppSettings.Config):
        env_file = ".env"
