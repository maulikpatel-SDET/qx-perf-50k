"""Service module 3550: business logic, no crypto."""


def calculate_total_3550(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3550():
    return 'module 3550 handles orders and invoices'
