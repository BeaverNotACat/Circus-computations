from decimal import Decimal
from typing import Any

from circus.applications.gateway import CoordinatesGenerator
from dependency_injector.wiring import Provide, inject


from circus.settings import Settings, SettingsContainer, settings


_sentinel: Any = object()


class AxisCoordicatesGeneratorGateway(CoordinatesGenerator):
    max_coord: Decimal
    min_coord: Decimal
    coord_step: Decimal

    def __init__(self) -> None:
        self.i = self.min_coord - self.coord_step

    def __next__(self) -> float:
        if self.i < self.max_coord - self.coord_step:
            self.i += self.coord_step
            return float(self.i)
        self.i = self.min_coord
        raise StopIteration

    def __iter__(self):
        return self


class XAxisCoordicatesGeneratorGateway(AxisCoordicatesGeneratorGateway):
    @inject
    def __init__(
        self, settings: Settings = Provide[SettingsContainer.settings]
    ) -> None:
        self.max_coord = settings.PLANE_X_SIZE / Decimal(settings.PLANE_X_SCALE)
        self.min_coord = -self.max_coord
        self.coord_step = 1 / Decimal(settings.PLANE_X_SCALE) / 10
        super().__init__()


class YAxisCoordicatesGeneratorGateway(AxisCoordicatesGeneratorGateway):
    @inject
    def __init__(
        self, settings: Settings = Provide[SettingsContainer.settings]
    ) -> None:
        self.max_coord = settings.PLANE_Y_SIZE / Decimal(settings.PLANE_Y_SCALE)
        self.min_coord = -self.max_coord
        self.coord_step = 1 / Decimal(settings.PLANE_Y_SCALE) / 10
        super().__init__()


class LineGeneratorGateway(AxisCoordicatesGeneratorGateway):
    @inject
    def __init__(self, max_coord: Decimal, min_coord: Decimal, coord_step: Decimal = 1 / Decimal(settings.PLANE_X_SCALE) / 10 ) -> None:
        self.max_coord = max_coord
        self.min_coord = min_coord
        self.coord_step = coord_step
        super().__init__()
