"""Service module 46991: business logic, no crypto."""


def calculate_total_46991(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46991():
    return 'module 46991 handles orders and invoices'
