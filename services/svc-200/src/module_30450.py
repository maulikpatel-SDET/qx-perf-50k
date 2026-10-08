"""Service module 30450: business logic, no crypto."""


def calculate_total_30450(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30450():
    return 'module 30450 handles orders and invoices'
