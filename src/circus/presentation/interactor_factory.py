from abc import ABC, abstractmethod
from typing import ContextManager, Iterable

from circus.applications.figures.coordinate_axes import DrawCoordinateAxes
from circus.applications.figures.function import DrawFunction
from circus.domain.models import Color, Function


class InteractorFactory(ABC):
    @abstractmethod
    def draw_function(self, color: Color, function: Function) -> ContextManager[DrawFunction]:
        raise NotImplementedError
    
    @abstractmethod
    def draw_coordinates(self, color: Color, function: Function) -> ContextManager[DrawCoordinateAxes]:
        raise NotImplementedError

    @abstractmethod
    def draw_area(self, color: Color, function: Iterable[Function]) -> ContextManager[DrawCoordinateAxes]:
        raise NotImplementedError

    @abstractmethod
    def show(self) -> ContextManager[DrawCoordinateAxes]:
        raise NotImplementedError
