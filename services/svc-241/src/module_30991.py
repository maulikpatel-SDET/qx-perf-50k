"""Service module 30991: business logic, no crypto."""


def calculate_total_30991(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30991():
    return 'module 30991 handles orders and invoices'
