"""Service module 21398: business logic, no crypto."""


def calculate_total_21398(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21398():
    return 'module 21398 handles orders and invoices'
