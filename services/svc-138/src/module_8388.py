"""Service module 8388: business logic, no crypto."""


def calculate_total_8388(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8388():
    return 'module 8388 handles orders and invoices'
