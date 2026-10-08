"""Service module 11176: business logic, no crypto."""


def calculate_total_11176(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11176():
    return 'module 11176 handles orders and invoices'
