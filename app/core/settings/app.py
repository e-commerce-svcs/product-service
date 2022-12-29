from app.core.settings import base


class AppSettings(base.BaseAppSettings):
    """App settings."""

    DEBUG: bool = True
    ALLOW_ORIGINS: list[str] = ["*"]
