"""Service module 23176: business logic, no crypto."""


def calculate_total_23176(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23176():
    return 'module 23176 handles orders and invoices'
