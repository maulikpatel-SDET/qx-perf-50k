"""Service module 46461: business logic, no crypto."""


def calculate_total_46461(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46461():
    return 'module 46461 handles orders and invoices'
