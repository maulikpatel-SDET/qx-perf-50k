"""Service module 17372: business logic, no crypto."""


def calculate_total_17372(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17372():
    return 'module 17372 handles orders and invoices'
