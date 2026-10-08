"""Service module 11778: business logic, no crypto."""


def calculate_total_11778(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11778():
    return 'module 11778 handles orders and invoices'
