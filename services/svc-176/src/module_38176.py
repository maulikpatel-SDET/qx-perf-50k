"""Service module 38176: business logic, no crypto."""


def calculate_total_38176(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38176():
    return 'module 38176 handles orders and invoices'
