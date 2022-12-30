import pydantic

from app.core.settings import base


class AppSettings(base.BaseAppSettings):
    """App settings."""

    # Set to True to enable debug mode.
    DEBUG: bool = True

    # CORS settings.
    ALLOW_ORIGINS: list[str] = ["*"]

    DATABASE_URL: pydantic.PostgresDsn = (
        "postgresql://postgres:postgres@localhost:5432/postgres"  # type: ignore
    )

    MIN_CONNECTION_COUNT: int = 10

    MAX_CONNECTION_COUNT: int = 20

    REDIS_URL: pydantic.RedisDsn = "redis://localhost:6379/0"  # type: ignore

    @property
    def sqlalchemy_kwargs(self) -> dict[str, bool | int]:
        return {
            "future": True,
            "pool_size": self.MIN_CONNECTION_COUNT,
            "max_overflow": self.MAX_CONNECTION_COUNT,
        }
