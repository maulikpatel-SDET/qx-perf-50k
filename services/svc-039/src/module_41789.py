"""Service module 41789: business logic, no crypto."""


def calculate_total_41789(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41789():
    return 'module 41789 handles orders and invoices'
