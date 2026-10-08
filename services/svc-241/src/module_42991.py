"""Service module 42991: business logic, no crypto."""


def calculate_total_42991(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42991():
    return 'module 42991 handles orders and invoices'
