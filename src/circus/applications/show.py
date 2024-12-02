from circus.applications.figure_interactor import FigureInteractor
from circus.applications.gateway import Plane


class Show(FigureInteractor[None]):
    plain_size: int

    def __init__(self, plain_gateway: Plane):
        self.plain = plain_gateway

    def __call__(self) -> None:
        self.plain.show()
