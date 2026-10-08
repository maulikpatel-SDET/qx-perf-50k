"""Service module 11398: business logic, no crypto."""


def calculate_total_11398(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11398():
    return 'module 11398 handles orders and invoices'
