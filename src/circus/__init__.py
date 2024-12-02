from dependency_injector import containers, providers

from circus.ioc import IoC
from circus.settings import Settings


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    wiring_config = containers.WiringConfiguration(
        modules=[__name__, "circus.presentation.interface"]
    )

    ioc = providers.Factory(IoC)
    settings = providers.Singleton(Settings)
