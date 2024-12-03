from dependency_injector import containers, providers
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    PLANE_X_SIZE: int = 500
    PLANE_Y_SIZE: int = 500
    PLANE_X_SCALE: float = 100
    PLANE_Y_SCALE: float = 20
    ROOTS_SEARCH_SCALE: float = 0.0064



settings = Settings()

class SettingsContainer(containers.DeclarativeContainer):
    config = providers.Configuration()
    wiring_config = containers.WiringConfiguration(
        modules=[
            "circus.adapters.plain",
            "circus.adapters.axis_generators",
            "circus.applications.figures.coordinate_axes",
            "circus.applications.figures.function",
            "circus.applications.figures.area",
        ]
    )

    settings = providers.Singleton(Settings)
