"""Service module 42848: business logic, no crypto."""


def calculate_total_42848(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42848():
    return 'module 42848 handles orders and invoices'
