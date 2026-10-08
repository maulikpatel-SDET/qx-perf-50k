"""Service module 16523: business logic, no crypto."""


def calculate_total_16523(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16523():
    return 'module 16523 handles orders and invoices'
