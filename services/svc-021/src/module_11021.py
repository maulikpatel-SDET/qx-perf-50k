"""Service module 11021: business logic, no crypto."""


def calculate_total_11021(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11021():
    return 'module 11021 handles orders and invoices'
