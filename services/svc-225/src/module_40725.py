"""Service module 40725: business logic, no crypto."""


def calculate_total_40725(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40725():
    return 'module 40725 handles orders and invoices'
