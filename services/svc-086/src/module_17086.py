"""Service module 17086: business logic, no crypto."""


def calculate_total_17086(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17086():
    return 'module 17086 handles orders and invoices'
