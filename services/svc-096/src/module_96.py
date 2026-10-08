"""Service module 96: business logic, no crypto."""


def calculate_total_96(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_96():
    return 'module 96 handles orders and invoices'
