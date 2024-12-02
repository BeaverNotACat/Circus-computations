from circus.applications.gateway import CLIOutput

from circus.domain.models import Coordinate, Function


class CLIOutputGateway(CLIOutput):
    def print_equation_roots(self, functions: list[Function], roots: list[Coordinate]) -> None:
        print("┏━━━━━━━━━━━━━┓")
        print("┃ FOUND ROOTS ┃")
        print("┗━━━━━━━━━━━━━┛")
        for root in roots:
            print(f" X = {root.x:,.2f}; Y = {root.y:,.2f}")
