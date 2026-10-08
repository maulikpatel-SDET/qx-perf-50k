"""Service module 42255: business logic, no crypto."""


def calculate_total_42255(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42255():
    return 'module 42255 handles orders and invoices'
