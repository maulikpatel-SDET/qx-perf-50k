"""Service module 1860: business logic, no crypto."""


def calculate_total_1860(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1860():
    return 'module 1860 handles orders and invoices'
