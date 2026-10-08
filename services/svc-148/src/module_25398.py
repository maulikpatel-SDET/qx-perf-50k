"""Service module 25398: business logic, no crypto."""


def calculate_total_25398(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25398():
    return 'module 25398 handles orders and invoices'
