"""Service module 7515: business logic, no crypto."""


def calculate_total_7515(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7515():
    return 'module 7515 handles orders and invoices'
