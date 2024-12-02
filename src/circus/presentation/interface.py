from math import sin, cos

from dependency_injector.wiring import inject, Provide

from circus.domain.models import Color, Function
from circus.ioc import IoC
from circus import Container

@inject
def run(ioc: IoC = Provide[Container.ioc]):
    with ioc.draw_coordinates() as action:
        action()
    sin_function = Function(Color.red, lambda x: cos(x))
    with ioc.draw_function() as action:
        action(sin_function)
    parabolic_function = Function(Color.red, lambda x: sin(x))
    with ioc.draw_function() as action:
        action(parabolic_function)
    with ioc.draw_area() as action:
        action([parabolic_function, sin_function])
    with ioc.show() as action:
        action()

    
