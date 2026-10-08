"""Service module 1365: business logic, no crypto."""


def calculate_total_1365(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1365():
    return 'module 1365 handles orders and invoices'
