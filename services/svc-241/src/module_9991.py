"""Service module 9991: business logic, no crypto."""


def calculate_total_9991(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9991():
    return 'module 9991 handles orders and invoices'
