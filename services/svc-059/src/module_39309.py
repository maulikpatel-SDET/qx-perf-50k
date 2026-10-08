"""Service module 39309: business logic, no crypto."""


def calculate_total_39309(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39309():
    return 'module 39309 handles orders and invoices'
