"""Service module 15604: business logic, no crypto."""


def calculate_total_15604(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15604():
    return 'module 15604 handles orders and invoices'
