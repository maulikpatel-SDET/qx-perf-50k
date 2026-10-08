"""Service module 18848: business logic, no crypto."""


def calculate_total_18848(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18848():
    return 'module 18848 handles orders and invoices'
