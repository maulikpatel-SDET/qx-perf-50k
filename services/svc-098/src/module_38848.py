"""Service module 38848: business logic, no crypto."""


def calculate_total_38848(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38848():
    return 'module 38848 handles orders and invoices'
