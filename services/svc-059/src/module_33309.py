"""Service module 33309: business logic, no crypto."""


def calculate_total_33309(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33309():
    return 'module 33309 handles orders and invoices'
