"""Service module 17468: business logic, no crypto."""


def calculate_total_17468(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17468():
    return 'module 17468 handles orders and invoices'
