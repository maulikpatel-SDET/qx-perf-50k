"""Service module 3991: business logic, no crypto."""


def calculate_total_3991(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3991():
    return 'module 3991 handles orders and invoices'
