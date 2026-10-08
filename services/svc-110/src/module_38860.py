"""Service module 38860: business logic, no crypto."""


def calculate_total_38860(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38860():
    return 'module 38860 handles orders and invoices'
