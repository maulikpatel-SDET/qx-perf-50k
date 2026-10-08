"""Service module 11510: business logic, no crypto."""


def calculate_total_11510(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11510():
    return 'module 11510 handles orders and invoices'
