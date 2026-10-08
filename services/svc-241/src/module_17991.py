"""Service module 17991: business logic, no crypto."""


def calculate_total_17991(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17991():
    return 'module 17991 handles orders and invoices'
