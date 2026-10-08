"""Service module 8515: business logic, no crypto."""


def calculate_total_8515(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8515():
    return 'module 8515 handles orders and invoices'
