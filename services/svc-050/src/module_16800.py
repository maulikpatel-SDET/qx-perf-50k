"""Service module 16800: business logic, no crypto."""


def calculate_total_16800(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16800():
    return 'module 16800 handles orders and invoices'
