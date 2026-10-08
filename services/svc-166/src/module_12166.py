"""Service module 12166: business logic, no crypto."""


def calculate_total_12166(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12166():
    return 'module 12166 handles orders and invoices'
