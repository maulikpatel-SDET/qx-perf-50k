"""Service module 7991: business logic, no crypto."""


def calculate_total_7991(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7991():
    return 'module 7991 handles orders and invoices'
