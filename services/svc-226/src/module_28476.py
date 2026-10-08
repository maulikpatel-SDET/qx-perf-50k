"""Service module 28476: business logic, no crypto."""


def calculate_total_28476(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28476():
    return 'module 28476 handles orders and invoices'
