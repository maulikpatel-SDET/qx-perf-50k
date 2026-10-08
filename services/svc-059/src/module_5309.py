"""Service module 5309: business logic, no crypto."""


def calculate_total_5309(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5309():
    return 'module 5309 handles orders and invoices'
