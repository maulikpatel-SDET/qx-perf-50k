"""Service module 13150: business logic, no crypto."""


def calculate_total_13150(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13150():
    return 'module 13150 handles orders and invoices'
