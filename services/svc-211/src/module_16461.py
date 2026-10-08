"""Service module 16461: business logic, no crypto."""


def calculate_total_16461(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16461():
    return 'module 16461 handles orders and invoices'
