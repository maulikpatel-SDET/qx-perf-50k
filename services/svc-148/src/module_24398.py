"""Service module 24398: business logic, no crypto."""


def calculate_total_24398(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24398():
    return 'module 24398 handles orders and invoices'
