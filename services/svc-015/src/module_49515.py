"""Service module 49515: business logic, no crypto."""


def calculate_total_49515(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49515():
    return 'module 49515 handles orders and invoices'
