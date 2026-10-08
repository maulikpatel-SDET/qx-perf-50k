"""Service module 1476: business logic, no crypto."""


def calculate_total_1476(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1476():
    return 'module 1476 handles orders and invoices'
