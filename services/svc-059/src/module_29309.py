"""Service module 29309: business logic, no crypto."""


def calculate_total_29309(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29309():
    return 'module 29309 handles orders and invoices'
