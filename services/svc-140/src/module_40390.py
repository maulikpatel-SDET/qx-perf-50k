"""Service module 40390: business logic, no crypto."""


def calculate_total_40390(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40390():
    return 'module 40390 handles orders and invoices'
