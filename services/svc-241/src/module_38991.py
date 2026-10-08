"""Service module 38991: business logic, no crypto."""


def calculate_total_38991(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38991():
    return 'module 38991 handles orders and invoices'
