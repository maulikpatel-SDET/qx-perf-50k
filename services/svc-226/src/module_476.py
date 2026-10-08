"""Service module 476: business logic, no crypto."""


def calculate_total_476(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_476():
    return 'module 476 handles orders and invoices'
