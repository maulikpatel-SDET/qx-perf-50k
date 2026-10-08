"""Service module 22550: business logic, no crypto."""


def calculate_total_22550(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22550():
    return 'module 22550 handles orders and invoices'
