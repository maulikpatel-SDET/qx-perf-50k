"""Service module 30515: business logic, no crypto."""


def calculate_total_30515(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30515():
    return 'module 30515 handles orders and invoices'
