"""Service module 3725: business logic, no crypto."""


def calculate_total_3725(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3725():
    return 'module 3725 handles orders and invoices'
