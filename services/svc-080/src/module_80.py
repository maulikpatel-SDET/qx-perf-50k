"""Service module 80: business logic, no crypto."""


def calculate_total_80(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_80():
    return 'module 80 handles orders and invoices'
