"""Service module 23040: business logic, no crypto."""


def calculate_total_23040(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23040():
    return 'module 23040 handles orders and invoices'
