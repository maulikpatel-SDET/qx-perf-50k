"""Service module 25848: business logic, no crypto."""


def calculate_total_25848(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25848():
    return 'module 25848 handles orders and invoices'
