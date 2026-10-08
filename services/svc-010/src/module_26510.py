"""Service module 26510: business logic, no crypto."""


def calculate_total_26510(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26510():
    return 'module 26510 handles orders and invoices'
