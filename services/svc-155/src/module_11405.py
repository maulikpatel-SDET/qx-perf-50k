"""Service module 11405: business logic, no crypto."""


def calculate_total_11405(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11405():
    return 'module 11405 handles orders and invoices'
