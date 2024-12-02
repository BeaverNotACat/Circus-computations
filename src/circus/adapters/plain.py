from dataclasses import dataclass

from circus.domain.models import Color, Coordinate, LineSegment
from circus.settings import Settings, SettingsContainer
from circus.applications.gateway import Plane

from dependency_injector.wiring import Provide, inject
from PIL import Image, ImageDraw , ImageFont


@dataclass
class ScreenCoordinates:
    x: int
    y: int


class PlainGateway(Plane):
    @inject
    def __init__(self, settings: Settings = Provide[SettingsContainer.settings]) -> None:
        self.settings = settings
        self._image = Image.new('RGB', (settings.PLANE_X_SIZE*2, settings.PLANE_Y_SIZE*2), 0xffffff)

    def _to_screen_coords(self, coords: Coordinate):
        x = int(coords.x * self.settings.PLANE_X_SCALE) + self.settings.PLANE_X_SIZE
        y = int(coords.y * -self.settings.PLANE_Y_SCALE) + self.settings.PLANE_Y_SIZE
        return ScreenCoordinates(x, y)
    
    def draw_dot(self, coordinate: Coordinate, color: Color) -> None:
        pixels = self._image.load()
        if pixels is None:
            raise Exception("Image is none")
        screen_coords = self._to_screen_coords(coordinate)
        try:
            if screen_coords.x <= 0:
                return
            if screen_coords.y <= 0:
                return
            pixels[screen_coords.x, screen_coords.y] = color
        except IndexError:
            pass
    
    def draw_line(self, line: LineSegment, color: Color) -> None:
        raise NotImplementedError

    def draw_text(self, text: str, coordinate: Coordinate, color: Color) -> None:
        draw = ImageDraw.Draw(self._image)
        font = ImageFont.truetype("FreeMonospaced.ttf", 20)
        screen_coordinates = self._to_screen_coords(coordinate)
        draw.text((screen_coordinates.x, screen_coordinates.y), text, color, font)

    def show(self):
        self._image.show()
