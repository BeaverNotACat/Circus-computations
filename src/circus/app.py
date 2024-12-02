from circus.presentation.interface import run
from circus import Container
from circus.settings import SettingsContainer



if __name__ == "__main__":
    container = Container()
    settings_container = SettingsContainer()
    run()
