"""Service module 17515: business logic, no crypto."""


def calculate_total_17515(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17515():
    return 'module 17515 handles orders and invoices'
