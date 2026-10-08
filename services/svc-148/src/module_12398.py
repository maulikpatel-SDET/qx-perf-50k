"""Service module 12398: business logic, no crypto."""


def calculate_total_12398(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12398():
    return 'module 12398 handles orders and invoices'
