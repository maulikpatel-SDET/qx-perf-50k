"""Service module 4610: business logic, no crypto."""


def calculate_total_4610(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4610():
    return 'module 4610 handles orders and invoices'
