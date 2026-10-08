"""Service module 16657: business logic, no crypto."""


def calculate_total_16657(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16657():
    return 'module 16657 handles orders and invoices'
