from circus.applications.figure_interactor import FigureInteractor
from circus.applications.gateway import CoordinatesGenerator, Plane
from circus.domain.models import Coordinate, Function


class DrawFunction(FigureInteractor[Function]):
    def __init__(self, plain_gateway: Plane, x_axis_gateway: CoordinatesGenerator):
        self.plain = plain_gateway
        self.axis = x_axis_gateway

    def __call__(self, input: Function) -> None:
        for x in self.axis:
            try:
                y = input.callable(x)
                self.plain.draw_dot(Coordinate(x, y), input.color)
            except ValueError:
                print("Divicion by zero")
