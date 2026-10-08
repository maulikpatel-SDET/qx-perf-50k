"""Service module 32991: business logic, no crypto."""


def calculate_total_32991(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32991():
    return 'module 32991 handles orders and invoices'
