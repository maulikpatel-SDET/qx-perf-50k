"""Service module 12723: business logic, no crypto."""


def calculate_total_12723(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12723():
    return 'module 12723 handles orders and invoices'
