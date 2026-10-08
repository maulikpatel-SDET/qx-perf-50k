"""Service module 44515: business logic, no crypto."""


def calculate_total_44515(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44515():
    return 'module 44515 handles orders and invoices'
