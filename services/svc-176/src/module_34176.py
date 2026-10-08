"""Service module 34176: business logic, no crypto."""


def calculate_total_34176(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34176():
    return 'module 34176 handles orders and invoices'
