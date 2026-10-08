"""Service module 2582: business logic, no crypto."""


def calculate_total_2582(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2582():
    return 'module 2582 handles orders and invoices'
