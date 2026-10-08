"""Service module 1979: business logic, no crypto."""


def calculate_total_1979(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1979():
    return 'module 1979 handles orders and invoices'
