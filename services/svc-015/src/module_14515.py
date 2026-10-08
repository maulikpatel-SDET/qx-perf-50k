"""Service module 14515: business logic, no crypto."""


def calculate_total_14515(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14515():
    return 'module 14515 handles orders and invoices'
