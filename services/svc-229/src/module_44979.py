"""Service module 44979: business logic, no crypto."""


def calculate_total_44979(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44979():
    return 'module 44979 handles orders and invoices'
