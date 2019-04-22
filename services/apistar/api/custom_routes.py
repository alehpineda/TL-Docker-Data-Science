from apistar import Route

def custom_route(name: str=None):
    """Print 42"""
    if name is None:
        name = "Talent Land"
    return "Hola {name}, 42 es la respuesta".format(**locals())

routes = [
    Route("/", method="GET", handler=custom_route),
]