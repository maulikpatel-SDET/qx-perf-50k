"""Service module 25661: business logic, no crypto."""


def calculate_total_25661(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25661():
    return 'module 25661 handles orders and invoices'
