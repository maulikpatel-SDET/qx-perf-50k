"""Service module 20848: business logic, no crypto."""


def calculate_total_20848(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20848():
    return 'module 20848 handles orders and invoices'
