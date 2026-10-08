"""Service module 20582: business logic, no crypto."""


def calculate_total_20582(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20582():
    return 'module 20582 handles orders and invoices'
