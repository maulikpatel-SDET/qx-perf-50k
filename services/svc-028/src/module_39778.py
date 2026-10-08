"""Service module 39778: business logic, no crypto."""


def calculate_total_39778(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39778():
    return 'module 39778 handles orders and invoices'
