"""Service module 15176: business logic, no crypto."""


def calculate_total_15176(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15176():
    return 'module 15176 handles orders and invoices'
