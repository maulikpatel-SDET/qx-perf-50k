"""Service module 23309: business logic, no crypto."""


def calculate_total_23309(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23309():
    return 'module 23309 handles orders and invoices'
