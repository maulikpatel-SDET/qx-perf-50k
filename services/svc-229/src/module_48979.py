"""Service module 48979: business logic, no crypto."""


def calculate_total_48979(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48979():
    return 'module 48979 handles orders and invoices'
