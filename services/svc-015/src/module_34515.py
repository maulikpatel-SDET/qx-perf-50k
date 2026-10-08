"""Service module 34515: business logic, no crypto."""


def calculate_total_34515(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34515():
    return 'module 34515 handles orders and invoices'
