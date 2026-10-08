"""Service module 23192: business logic, no crypto."""


def calculate_total_23192(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23192():
    return 'module 23192 handles orders and invoices'
