"""Service module 10515: business logic, no crypto."""


def calculate_total_10515(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10515():
    return 'module 10515 handles orders and invoices'
