"""Service module 3388: business logic, no crypto."""


def calculate_total_3388(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3388():
    return 'module 3388 handles orders and invoices'
