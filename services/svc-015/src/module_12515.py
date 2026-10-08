"""Service module 12515: business logic, no crypto."""


def calculate_total_12515(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12515():
    return 'module 12515 handles orders and invoices'
