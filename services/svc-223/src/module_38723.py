"""Service module 38723: business logic, no crypto."""


def calculate_total_38723(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38723():
    return 'module 38723 handles orders and invoices'
