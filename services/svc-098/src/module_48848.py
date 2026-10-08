"""Service module 48848: business logic, no crypto."""


def calculate_total_48848(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48848():
    return 'module 48848 handles orders and invoices'
