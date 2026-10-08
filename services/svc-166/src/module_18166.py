"""Service module 18166: business logic, no crypto."""


def calculate_total_18166(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18166():
    return 'module 18166 handles orders and invoices'
