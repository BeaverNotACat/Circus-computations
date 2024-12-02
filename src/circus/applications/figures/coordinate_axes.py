from decimal import Decimal
from typing import Protocol

from dependency_injector.wiring import inject, Provide

from circus.applications.figure_interactor import FigureInteractor
from circus.applications.gateway import CoordinatesGenerator, Plane
from circus.domain.models import Color, Coordinate
from circus.settings import Settings, SettingsContainer



class PlaneGateway(Plane, Protocol): ...
class AxisCoordinatesGenerator(CoordinatesGenerator, Protocol): ...


class DrawCoordinateAxes(FigureInteractor[None]):
    plain_size: int
    price_step: int

    @inject
    def __init__(
        self,
        plain_gateway: PlaneGateway,
        x_axis_gateway: CoordinatesGenerator,
        y_axis_gateway: CoordinatesGenerator,
        settings: Settings = Provide[SettingsContainer.settings],
    ):
        self.plain = plain_gateway
        self.x_axis = x_axis_gateway
        self.y_axis = y_axis_gateway
        self.settings = settings

    def __call__(self):
        self._draw_axes()
        self._draw_price()
        self._draw_small_price()

    def _draw_axes(self):
        for x in self.x_axis:
            self.plain.draw_dot(Coordinate(x, 0), color=Color.black)
        for y in self.y_axis:
            self.plain.draw_dot(Coordinate(0, y), color=Color.black)

    def _draw_price(self):
        price_x_mark = 5 / Decimal(self.settings.PLANE_X_SCALE)
        price_y_mark = 5 / Decimal(self.settings.PLANE_X_SCALE)
        x_step = 1 / Decimal(self.settings.PLANE_X_SCALE)
        y_step = 1 / Decimal(self.settings.PLANE_Y_SCALE)

        for x in self.x_axis:
            if not x.is_integer():
                continue
            y = -price_y_mark
            while y < price_y_mark:
                self.plain.draw_dot(Coordinate(x, float(y)), color=Color.black)
                y += y_step
            self.plain.draw_text(str(x),Coordinate(x, float(y*5)), Color.black)
        for y in self.y_axis:
            if not y.is_integer() or y == 0:
                continue
            self.plain.draw_dot(Coordinate(0, y), color=Color.black)
            x = -price_x_mark
            while x < price_x_mark:
                self.plain.draw_dot(Coordinate(float(x), y), color=Color.black)
                x += x_step
            self.plain.draw_text(str(y),Coordinate(float(x*2), y), Color.black)

    def _draw_small_price(self):
        price_x_mark = 2 / Decimal(self.settings.PLANE_X_SCALE)
        price_y_mark = 2 / Decimal(self.settings.PLANE_Y_SCALE)
        x_step = 1 / Decimal(self.settings.PLANE_X_SCALE)
        y_step = 1 / Decimal(self.settings.PLANE_Y_SCALE)

        for x in self.x_axis:
            if not (x * 10).is_integer():
                continue
            y = -price_y_mark
            while y < price_y_mark:
                self.plain.draw_dot(Coordinate(x, float(y)), color=Color.black)
                y += y_step
        for y in self.y_axis:
            if not (y * 10).is_integer():
                continue
            self.plain.draw_dot(Coordinate(0, y), color=Color.black)
            x = -price_x_mark
            while x < price_x_mark:
                self.plain.draw_dot(Coordinate(float(x), y), color=Color.black)
                x += x_step
