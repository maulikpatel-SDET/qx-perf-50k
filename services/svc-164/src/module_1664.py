"""Service module 1664: business logic, no crypto."""


def calculate_total_1664(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1664():
    return 'module 1664 handles orders and invoices'
