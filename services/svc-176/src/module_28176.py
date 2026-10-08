"""Service module 28176: business logic, no crypto."""


def calculate_total_28176(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28176():
    return 'module 28176 handles orders and invoices'
