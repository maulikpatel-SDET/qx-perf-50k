"""Service module 47758: business logic, no crypto."""


def calculate_total_47758(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47758():
    return 'module 47758 handles orders and invoices'
