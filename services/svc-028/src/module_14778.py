"""Service module 14778: business logic, no crypto."""


def calculate_total_14778(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14778():
    return 'module 14778 handles orders and invoices'
