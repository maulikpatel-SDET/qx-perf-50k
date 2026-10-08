"""Service module 12593: business logic, no crypto."""


def calculate_total_12593(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12593():
    return 'module 12593 handles orders and invoices'
