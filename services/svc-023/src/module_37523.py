"""Service module 37523: business logic, no crypto."""


def calculate_total_37523(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37523():
    return 'module 37523 handles orders and invoices'
