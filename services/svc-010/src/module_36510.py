"""Service module 36510: business logic, no crypto."""


def calculate_total_36510(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36510():
    return 'module 36510 handles orders and invoices'
