"""Service module 661: business logic, no crypto."""


def calculate_total_661(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_661():
    return 'module 661 handles orders and invoices'
