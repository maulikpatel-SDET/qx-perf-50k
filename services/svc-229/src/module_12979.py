"""Service module 12979: business logic, no crypto."""


def calculate_total_12979(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12979():
    return 'module 12979 handles orders and invoices'
