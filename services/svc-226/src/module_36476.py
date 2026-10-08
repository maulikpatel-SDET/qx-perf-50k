"""Service module 36476: business logic, no crypto."""


def calculate_total_36476(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36476():
    return 'module 36476 handles orders and invoices'
