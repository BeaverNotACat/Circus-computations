from typing import Callable, TypeVar, Protocol


InputDTO = TypeVar("InputDTO")


class FigureInteractor[InputDTO](Protocol):
    def __call__(self, input: InputDTO) -> None:
        raise NotImplementedError
