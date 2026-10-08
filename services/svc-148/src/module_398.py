"""Service module 398: business logic, no crypto."""


def calculate_total_398(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_398():
    return 'module 398 handles orders and invoices'
