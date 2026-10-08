"""Service module 12255: business logic, no crypto."""


def calculate_total_12255(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12255():
    return 'module 12255 handles orders and invoices'
