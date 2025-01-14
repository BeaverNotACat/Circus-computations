from circus.applications.figure_interactor import FigureInteractor
from circus.applications.gateway import CoordinatesGenerator, Plain
from circus.domain.models import Coordinate, Function, LineSegment


class DrawFunction(FigureInteractor[Function]):
    def __init__(self, plain_gateway: Plain, x_axis_gateway: CoordinatesGenerator):
        self.plain = plain_gateway
        self.axis = x_axis_gateway

    def __call__(self, input: Function) -> None:
        axis = list(self.axis)
        for x1, x2 in zip(axis[:-1], axis[1:]):
            try:
                y1 = input.callable(x1)
                y2 = input.callable(x2)
                self.plain.draw_line(
                    LineSegment(Coordinate(x1, y1), Coordinate(x2, y2)), input.color
                )
            except ValueError:
                print("Divicion by zero")
