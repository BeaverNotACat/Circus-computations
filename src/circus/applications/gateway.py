from typing import Protocol, Self

from circus.domain.models import Color, Coordinate, LineSegment, Function


class Plain(Protocol):
    def draw_dot(self, coordinate: Coordinate, color: Color) -> None:
        raise NotImplementedError

    def draw_line(self, line: LineSegment,  color: Color) -> None:
        raise NotImplementedError

    def draw_text(self, text: str, coordinate: Coordinate, color: Color) -> None:
        raise NotImplementedError

    def show(self):
        raise NotImplementedError


class CLIOutput(Protocol):
    def print_equation_roots(self, functions: list[Function], roots: list[Coordinate]) -> None:
        raise NotImplementedError


class CoordinatesGenerator(Protocol):
    def __next__(self) -> float:
        raise NotImplementedError

    def __iter__(self) -> Self:
        raise NotImplementedError
        
