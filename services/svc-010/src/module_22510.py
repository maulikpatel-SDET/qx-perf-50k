"""Service module 22510: business logic, no crypto."""


def calculate_total_22510(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22510():
    return 'module 22510 handles orders and invoices'
