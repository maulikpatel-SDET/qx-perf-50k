"""Service module 13510: business logic, no crypto."""


def calculate_total_13510(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13510():
    return 'module 13510 handles orders and invoices'
