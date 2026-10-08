"""Service module 46176: business logic, no crypto."""


def calculate_total_46176(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46176():
    return 'module 46176 handles orders and invoices'
