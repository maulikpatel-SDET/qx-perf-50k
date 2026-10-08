"""Service module 17657: business logic, no crypto."""


def calculate_total_17657(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17657():
    return 'module 17657 handles orders and invoices'
