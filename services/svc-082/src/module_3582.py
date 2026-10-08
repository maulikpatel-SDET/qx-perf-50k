"""Service module 3582: business logic, no crypto."""


def calculate_total_3582(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3582():
    return 'module 3582 handles orders and invoices'
