"""Service module 6786: business logic, no crypto."""


def calculate_total_6786(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6786():
    return 'module 6786 handles orders and invoices'
