"""Service module 3687: business logic, no crypto."""


def calculate_total_3687(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3687():
    return 'module 3687 handles orders and invoices'
