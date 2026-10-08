"""Service module 22398: business logic, no crypto."""


def calculate_total_22398(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22398():
    return 'module 22398 handles orders and invoices'
