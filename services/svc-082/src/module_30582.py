"""Service module 30582: business logic, no crypto."""


def calculate_total_30582(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30582():
    return 'module 30582 handles orders and invoices'
