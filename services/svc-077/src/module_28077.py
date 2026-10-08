"""Service module 28077: business logic, no crypto."""


def calculate_total_28077(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28077():
    return 'module 28077 handles orders and invoices'
