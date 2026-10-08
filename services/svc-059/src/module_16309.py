"""Service module 16309: business logic, no crypto."""


def calculate_total_16309(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16309():
    return 'module 16309 handles orders and invoices'
