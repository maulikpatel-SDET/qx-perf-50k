"""Service module 12550: business logic, no crypto."""


def calculate_total_12550(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12550():
    return 'module 12550 handles orders and invoices'
