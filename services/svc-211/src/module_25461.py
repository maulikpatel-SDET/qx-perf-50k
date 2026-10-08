"""Service module 25461: business logic, no crypto."""


def calculate_total_25461(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25461():
    return 'module 25461 handles orders and invoices'
