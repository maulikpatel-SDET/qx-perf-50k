"""Service module 49398: business logic, no crypto."""


def calculate_total_49398(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49398():
    return 'module 49398 handles orders and invoices'
