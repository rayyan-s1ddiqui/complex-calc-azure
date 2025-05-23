import sympy as sp

# Predefined variables available to users
x, y, z = sp.symbols("x y z")
safe_dict = {**sp.__dict__, "x": x, "y": y, "z": z}

def crunch(expression: str):
    try:
        expr = sp.sympify(expression, locals=safe_dict)
        result = sp.simplify(expr)
        return result
    except Exception as e:
        return f"Error: {e}"
