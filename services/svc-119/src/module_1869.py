"""Service module 1869: business logic, no crypto."""


def calculate_total_1869(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1869():
    return 'module 1869 handles orders and invoices'
