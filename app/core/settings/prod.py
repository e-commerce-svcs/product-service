from app.core.settings.app import AppSettings


class ProdAppSettings(AppSettings):
    DEBUG: bool = False

    class Config(AppSettings.Config):
        env_file = ".env"
