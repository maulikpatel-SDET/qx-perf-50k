"""Service module 28266: business logic, no crypto."""


def calculate_total_28266(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28266():
    return 'module 28266 handles orders and invoices'
