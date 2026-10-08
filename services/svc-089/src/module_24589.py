"""Service module 24589: business logic, no crypto."""


def calculate_total_24589(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24589():
    return 'module 24589 handles orders and invoices'
