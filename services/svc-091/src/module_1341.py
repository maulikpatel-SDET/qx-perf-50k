"""Service module 1341: business logic, no crypto."""


def calculate_total_1341(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1341():
    return 'module 1341 handles orders and invoices'
