"""Service module 12635: business logic, no crypto."""


def calculate_total_12635(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12635():
    return 'module 12635 handles orders and invoices'
