"""Service module 22604: business logic, no crypto."""


def calculate_total_22604(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22604():
    return 'module 22604 handles orders and invoices'
