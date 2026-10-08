"""Service module 26176: business logic, no crypto."""


def calculate_total_26176(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26176():
    return 'module 26176 handles orders and invoices'
