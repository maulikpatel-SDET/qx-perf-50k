"""Service module 30550: business logic, no crypto."""


def calculate_total_30550(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30550():
    return 'module 30550 handles orders and invoices'
