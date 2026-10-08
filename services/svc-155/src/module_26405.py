"""Service module 26405: business logic, no crypto."""


def calculate_total_26405(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26405():
    return 'module 26405 handles orders and invoices'
