"""Service module 13991: business logic, no crypto."""


def calculate_total_13991(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13991():
    return 'module 13991 handles orders and invoices'
