"""Service module 14309: business logic, no crypto."""


def calculate_total_14309(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14309():
    return 'module 14309 handles orders and invoices'
