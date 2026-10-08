"""Service module 16021: business logic, no crypto."""


def calculate_total_16021(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16021():
    return 'module 16021 handles orders and invoices'
