"""Service module 42829: business logic, no crypto."""


def calculate_total_42829(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42829():
    return 'module 42829 handles orders and invoices'
