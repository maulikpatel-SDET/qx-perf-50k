"""Service module 47991: business logic, no crypto."""


def calculate_total_47991(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47991():
    return 'module 47991 handles orders and invoices'
