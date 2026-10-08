"""Service module 40176: business logic, no crypto."""


def calculate_total_40176(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40176():
    return 'module 40176 handles orders and invoices'
