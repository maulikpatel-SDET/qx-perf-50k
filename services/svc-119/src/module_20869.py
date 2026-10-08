"""Service module 20869: business logic, no crypto."""


def calculate_total_20869(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20869():
    return 'module 20869 handles orders and invoices'
