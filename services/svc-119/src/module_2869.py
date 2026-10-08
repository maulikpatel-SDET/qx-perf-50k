"""Service module 2869: business logic, no crypto."""


def calculate_total_2869(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2869():
    return 'module 2869 handles orders and invoices'
