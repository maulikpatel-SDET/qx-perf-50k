"""Service module 28763: business logic, no crypto."""


def calculate_total_28763(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28763():
    return 'module 28763 handles orders and invoices'
