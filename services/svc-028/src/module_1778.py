"""Service module 1778: business logic, no crypto."""


def calculate_total_1778(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1778():
    return 'module 1778 handles orders and invoices'
