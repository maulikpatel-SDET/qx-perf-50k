"""Service module 3176: business logic, no crypto."""


def calculate_total_3176(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3176():
    return 'module 3176 handles orders and invoices'
