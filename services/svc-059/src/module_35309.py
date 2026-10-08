"""Service module 35309: business logic, no crypto."""


def calculate_total_35309(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35309():
    return 'module 35309 handles orders and invoices'
