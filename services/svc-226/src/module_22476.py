"""Service module 22476: business logic, no crypto."""


def calculate_total_22476(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22476():
    return 'module 22476 handles orders and invoices'
