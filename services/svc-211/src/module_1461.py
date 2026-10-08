"""Service module 1461: business logic, no crypto."""


def calculate_total_1461(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1461():
    return 'module 1461 handles orders and invoices'
