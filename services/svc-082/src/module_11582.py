"""Service module 11582: business logic, no crypto."""


def calculate_total_11582(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11582():
    return 'module 11582 handles orders and invoices'
