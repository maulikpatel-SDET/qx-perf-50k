"""Service module 20638: business logic, no crypto."""


def calculate_total_20638(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20638():
    return 'module 20638 handles orders and invoices'
