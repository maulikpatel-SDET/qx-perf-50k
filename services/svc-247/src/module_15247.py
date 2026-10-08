"""Service module 15247: business logic, no crypto."""


def calculate_total_15247(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15247():
    return 'module 15247 handles orders and invoices'
