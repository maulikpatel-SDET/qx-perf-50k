"""Service module 49979: business logic, no crypto."""


def calculate_total_49979(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49979():
    return 'module 49979 handles orders and invoices'
