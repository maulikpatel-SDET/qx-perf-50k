"""Service module 15848: business logic, no crypto."""


def calculate_total_15848(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15848():
    return 'module 15848 handles orders and invoices'
