from circus.applications.figure_interactor import FigureInteractor
from circus.applications.gateway import Plain


class Show(FigureInteractor[None]):
    plain_size: int

    def __init__(self, plain_gateway: Plain):
        self.plain = plain_gateway

    def __call__(self) -> None:
        self.plain.show()
