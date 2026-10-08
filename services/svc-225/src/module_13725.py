"""Service module 13725: business logic, no crypto."""


def calculate_total_13725(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13725():
    return 'module 13725 handles orders and invoices'
