"""Service module 23321: business logic, no crypto."""


def calculate_total_23321(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23321():
    return 'module 23321 handles orders and invoices'
