"""Service module 12674: business logic, no crypto."""


def calculate_total_12674(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12674():
    return 'module 12674 handles orders and invoices'
