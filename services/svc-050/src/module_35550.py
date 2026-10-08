"""Service module 35550: business logic, no crypto."""


def calculate_total_35550(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35550():
    return 'module 35550 handles orders and invoices'
