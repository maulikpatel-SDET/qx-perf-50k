"""Service module 36550: business logic, no crypto."""


def calculate_total_36550(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36550():
    return 'module 36550 handles orders and invoices'
