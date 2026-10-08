"""Service module 3398: business logic, no crypto."""


def calculate_total_3398(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3398():
    return 'module 3398 handles orders and invoices'
