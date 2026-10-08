"""Service module 15860: business logic, no crypto."""


def calculate_total_15860(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15860():
    return 'module 15860 handles orders and invoices'
