"""Service module 3848: business logic, no crypto."""


def calculate_total_3848(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3848():
    return 'module 3848 handles orders and invoices'
