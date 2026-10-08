"""Service module 12604: business logic, no crypto."""


def calculate_total_12604(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12604():
    return 'module 12604 handles orders and invoices'
