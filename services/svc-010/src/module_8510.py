"""Service module 8510: business logic, no crypto."""


def calculate_total_8510(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8510():
    return 'module 8510 handles orders and invoices'
