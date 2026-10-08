"""Service module 39166: business logic, no crypto."""


def calculate_total_39166(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39166():
    return 'module 39166 handles orders and invoices'
