"""Service module 46661: business logic, no crypto."""


def calculate_total_46661(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46661():
    return 'module 46661 handles orders and invoices'
