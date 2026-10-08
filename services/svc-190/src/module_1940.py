"""Service module 1940: business logic, no crypto."""


def calculate_total_1940(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1940():
    return 'module 1940 handles orders and invoices'
