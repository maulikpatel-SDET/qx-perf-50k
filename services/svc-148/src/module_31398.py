"""Service module 31398: business logic, no crypto."""


def calculate_total_31398(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31398():
    return 'module 31398 handles orders and invoices'
