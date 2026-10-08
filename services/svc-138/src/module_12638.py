"""Service module 12638: business logic, no crypto."""


def calculate_total_12638(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12638():
    return 'module 12638 handles orders and invoices'
