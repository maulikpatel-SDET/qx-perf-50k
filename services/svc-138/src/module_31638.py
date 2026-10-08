"""Service module 31638: business logic, no crypto."""


def calculate_total_31638(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31638():
    return 'module 31638 handles orders and invoices'
