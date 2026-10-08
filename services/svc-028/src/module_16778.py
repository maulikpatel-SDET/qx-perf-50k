"""Service module 16778: business logic, no crypto."""


def calculate_total_16778(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16778():
    return 'module 16778 handles orders and invoices'
