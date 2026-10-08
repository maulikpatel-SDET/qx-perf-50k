"""Service module 14991: business logic, no crypto."""


def calculate_total_14991(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14991():
    return 'module 14991 handles orders and invoices'
