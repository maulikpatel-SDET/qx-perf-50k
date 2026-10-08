"""Service module 42869: business logic, no crypto."""


def calculate_total_42869(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42869():
    return 'module 42869 handles orders and invoices'
