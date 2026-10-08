"""Service module 23180: business logic, no crypto."""


def calculate_total_23180(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23180():
    return 'module 23180 handles orders and invoices'
