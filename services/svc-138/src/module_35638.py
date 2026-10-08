"""Service module 35638: business logic, no crypto."""


def calculate_total_35638(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35638():
    return 'module 35638 handles orders and invoices'
