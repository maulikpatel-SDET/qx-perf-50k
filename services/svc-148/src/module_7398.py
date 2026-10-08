"""Service module 7398: business logic, no crypto."""


def calculate_total_7398(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7398():
    return 'module 7398 handles orders and invoices'
