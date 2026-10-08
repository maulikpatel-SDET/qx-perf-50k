"""Service module 15869: business logic, no crypto."""


def calculate_total_15869(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15869():
    return 'module 15869 handles orders and invoices'
