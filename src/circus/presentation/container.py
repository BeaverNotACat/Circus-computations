
from dependency_injector import containers, providers


class InteractorContainer(containers.DeclarativeContainer):
    config = providers.Configuration()



interactor_container = InteractorContainer()
