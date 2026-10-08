"""Service module 24723: business logic, no crypto."""


def calculate_total_24723(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24723():
    return 'module 24723 handles orders and invoices'
