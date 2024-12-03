from math import sin, cos

from dependency_injector.wiring import inject, Provide

from circus.domain.models import Color, Function
from circus.ioc import IoC
from circus import Container

@inject
def run(ioc: IoC = Provide[Container.ioc]):
    with ioc.draw_coordinates() as action:
        action()
    f1 = Function(Color.red, lambda x: x**3-8*x+1)
    with ioc.draw_function() as action:
        action(f1)
    f2 = Function(Color.blue, lambda x: -12*sin(x)-10*cos(x))
    with ioc.draw_function() as action:
        action(f2)
    with ioc.draw_area() as action:
        action((f2, f1))
    with ioc.show() as action:
        action()

    
