import importlib
from rolldice import roll_dice

def get_renderer(renderer):
    render_module = importlib.import_module("render.%s"%(renderer))

def get_result(expression):
    ans, explanation = roll_dice(expression)
    return (expression, ans, explanation)

def enact_expressions(expressions, renderer, args):
    # build a data structure to pass to the renderer
    result = map(get_result, expressions)

    renderer.render(result, args)
