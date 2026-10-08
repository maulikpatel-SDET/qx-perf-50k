"""Service module 12387: business logic, no crypto."""


def calculate_total_12387(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12387():
    return 'module 12387 handles orders and invoices'
