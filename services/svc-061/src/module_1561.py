"""Service module 1561: business logic, no crypto."""


def calculate_total_1561(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1561():
    return 'module 1561 handles orders and invoices'
