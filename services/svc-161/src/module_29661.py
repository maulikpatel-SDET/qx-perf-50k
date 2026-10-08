"""Service module 29661: business logic, no crypto."""


def calculate_total_29661(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29661():
    return 'module 29661 handles orders and invoices'
