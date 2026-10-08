"""Service module 26789: business logic, no crypto."""


def calculate_total_26789(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26789():
    return 'module 26789 handles orders and invoices'
