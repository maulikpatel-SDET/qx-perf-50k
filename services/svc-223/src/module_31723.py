"""Service module 31723: business logic, no crypto."""


def calculate_total_31723(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31723():
    return 'module 31723 handles orders and invoices'
