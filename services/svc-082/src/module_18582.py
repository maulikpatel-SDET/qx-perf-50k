"""Service module 18582: business logic, no crypto."""


def calculate_total_18582(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18582():
    return 'module 18582 handles orders and invoices'
