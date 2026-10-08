"""Service module 26725: business logic, no crypto."""


def calculate_total_26725(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26725():
    return 'module 26725 handles orders and invoices'
