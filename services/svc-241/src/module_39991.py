"""Service module 39991: business logic, no crypto."""


def calculate_total_39991(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39991():
    return 'module 39991 handles orders and invoices'
