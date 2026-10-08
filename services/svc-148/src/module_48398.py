"""Service module 48398: business logic, no crypto."""


def calculate_total_48398(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48398():
    return 'module 48398 handles orders and invoices'
