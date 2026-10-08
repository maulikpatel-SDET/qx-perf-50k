"""Service module 36582: business logic, no crypto."""


def calculate_total_36582(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36582():
    return 'module 36582 handles orders and invoices'
