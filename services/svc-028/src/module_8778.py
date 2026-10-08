"""Service module 8778: business logic, no crypto."""


def calculate_total_8778(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8778():
    return 'module 8778 handles orders and invoices'
