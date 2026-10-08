"""Service module 11979: business logic, no crypto."""


def calculate_total_11979(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11979():
    return 'module 11979 handles orders and invoices'
