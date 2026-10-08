"""Service module 6476: business logic, no crypto."""


def calculate_total_6476(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6476():
    return 'module 6476 handles orders and invoices'
