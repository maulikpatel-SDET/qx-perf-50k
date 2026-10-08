"""Service module 515: business logic, no crypto."""


def calculate_total_515(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_515():
    return 'module 515 handles orders and invoices'
