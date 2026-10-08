"""Service module 46004: business logic, no crypto."""


def calculate_total_46004(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46004():
    return 'module 46004 handles orders and invoices'
