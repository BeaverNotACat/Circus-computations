from typing import Type
from decimal import Decimal

from dependency_injector.wiring import Provide

from circus.settings import SettingsContainer, Settings
from circus.applications.figure_interactor import FigureInteractor
from circus.applications.gateway import CoordinatesGenerator, Plain, CLIOutput
from circus.domain.models import Color, Coordinate, Function

from circus.adapters.axis_generators import (
    LineGeneratorGateway,
)  # TODO Make protocol for this


class DrawArea(FigureInteractor[list[Function]]):
    def __init__(
        self,
        plain_gateway: Plain,
        x_axis_gateway: CoordinatesGenerator,
        y_axis_gateway: CoordinatesGenerator,
        cli_gateway: CLIOutput,
        line_generator_factory: Type[LineGeneratorGateway],
        settings: Settings = Provide[SettingsContainer.settings],
    ):
        self.plain = plain_gateway
        self.x_axis = x_axis_gateway
        self.y_axis = y_axis_gateway
        self.cli = cli_gateway
        self.line_generator_factory = line_generator_factory
        self.search_scale = settings.ROOTS_SEARCH_SCALE
        # self.search_scale = 1 / Decimal(settings.PLANE_X_SCALE)
        self.plain_size = settings.PLANE_X_SIZE / Decimal(settings.PLANE_X_SCALE)
        self.area_coord_step = 1 / Decimal(settings.PLANE_X_SCALE) / 10
        self.area_hash_step = line_generator_factory(
            settings.PLANE_Y_SIZE / Decimal(settings.PLANE_Y_SCALE),
            -settings.PLANE_Y_SIZE / Decimal(settings.PLANE_Y_SCALE),
            1 / Decimal(settings.PLANE_Y_SCALE) * 10,
        )

    def _find_roots(self, functions: list[Function]):  # TODO Fix error accumulation
        found_roots = []
        for x in self.x_axis:
            x = round(x, 3)
            results = list(map(lambda function: function.callable(x), functions))
            y_max = round(max(results), 3)
            y_min = round(min(results), 3)
            if (y_max - y_min) < self.search_scale:
                found_roots.append(Coordinate(x, y_max))
        return found_roots

    def _integral(self, function: Function, x_start: float, x_end: float):
        """Trapezoidal rule"""
        f_start = function.callable(x_start)
        f_end = function.callable(x_end)
        f_mid = sum(
            function.callable(x)
            for x in self.line_generator_factory(Decimal(x_end), Decimal(x_start))
        )
        return ((f_start + f_end / 2) + f_mid) * float(self.area_coord_step)

    def _caculate_areas(
        self, f1: Function, f2: Function, roots: list[Coordinate]
    ) -> list[float]:
        areas = []
        for coord1, coord2 in zip(roots[:-1:], roots[1::]):
            f1_integral = self._integral(f1, coord1.x, coord2.x)
            f2_integral = self._integral(f2, coord1.x, coord2.x)
            areas.append(abs(f1_integral - f2_integral))
        return areas

    def _draw_areas(
        self, f1: Function, f2: Function, roots: list[Coordinate], areas: list[float]
    ) -> None:
        for coord1, coord2, area in zip(roots[:-1], roots[1:], areas):
            text_coords = Coordinate(
                (coord1.x + coord2.x) / 2, (coord1.y + coord2.y) / 2
            )
            for x in self.line_generator_factory(Decimal(coord2.x),Decimal(coord1.x)):
                for t in self.area_hash_step:
                    y = x + t
                    max_fy = max(f1.callable(x), f2.callable(x))
                    min_fy = min(f1.callable(x), f2.callable(x))
                    if max_fy > y > min_fy:
                        self.plain.draw_dot(Coordinate(x, y), Color.green)

            self.plain.draw_text(f"{area:,.2f}", text_coords, Color.green)

    def __call__(self, input: tuple[Function, Function]) -> None:
        roots = self._find_roots(list(input))
        self.cli.print_equation_roots(list(input), roots)

        areas = self._caculate_areas(input[0], input[1], roots)
        self._draw_areas(input[0], input[1], roots, areas)
