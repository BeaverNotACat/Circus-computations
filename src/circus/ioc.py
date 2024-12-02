from contextlib import contextmanager

from circus.adapters.cli import CLIOutputGateway
from circus.adapters.plain import PlainGateway
from circus.adapters.axis_generators import (
    XAxisCoordicatesGeneratorGateway,
    YAxisCoordicatesGeneratorGateway,
    LineGeneratorGateway
)
from circus.applications.figures.coordinate_axes import DrawCoordinateAxes
from circus.applications.figures.function import DrawFunction
from circus.applications.figures.area import DrawArea
from circus.applications.show import Show
from circus.domain.models import Color, Function


class IoC:
    def __init__(self):
        self.plain_gateway = PlainGateway()
        self.x_axis_gateway = XAxisCoordicatesGeneratorGateway()
        self.y_axis_gateway = YAxisCoordicatesGeneratorGateway()
        self.line_axis_factory = LineGeneratorGateway
        self.cli_gateway = CLIOutputGateway()

    @contextmanager
    def draw_function(self):
        yield DrawFunction(self.plain_gateway, self.x_axis_gateway)
    
    @contextmanager
    def draw_coordinates(self):
        yield DrawCoordinateAxes(self.plain_gateway, self.x_axis_gateway, self.y_axis_gateway)
    
    @contextmanager
    def draw_area(self):
        yield DrawArea(self.plain_gateway, self.x_axis_gateway, self.y_axis_gateway, self.cli_gateway, self.line_axis_factory)
    
    @contextmanager
    def show(self):
        yield Show(self.plain_gateway)
