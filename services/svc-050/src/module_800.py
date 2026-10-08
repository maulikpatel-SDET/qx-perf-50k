"""Service module 800: business logic, no crypto."""


def calculate_total_800(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_800():
    return 'module 800 handles orders and invoices'
