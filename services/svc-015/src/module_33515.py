"""Service module 33515: business logic, no crypto."""


def calculate_total_33515(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33515():
    return 'module 33515 handles orders and invoices'
