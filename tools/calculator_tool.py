import operator

def calculate(expression):
    """Calculates the result of a simple arithmetic expression."""
    ops = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }
    parts = expression.split()
    if len(parts) != 3:
        return "Invalid expression"
    num1, op, num2 = parts
    if op not in ops:
        return f"Unknown operator: {op}"
    try:
        return ops[op](float(num1), float(num2))
    except ValueError:
        return "Invalid numbers"
