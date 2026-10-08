"""Service module 36979: business logic, no crypto."""


def calculate_total_36979(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36979():
    return 'module 36979 handles orders and invoices'
