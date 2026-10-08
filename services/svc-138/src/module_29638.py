"""Service module 29638: business logic, no crypto."""


def calculate_total_29638(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29638():
    return 'module 29638 handles orders and invoices'
