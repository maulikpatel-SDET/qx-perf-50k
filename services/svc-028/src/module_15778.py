"""Service module 15778: business logic, no crypto."""


def calculate_total_15778(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15778():
    return 'module 15778 handles orders and invoices'
