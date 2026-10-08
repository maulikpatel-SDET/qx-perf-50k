"""Service module 758: business logic, no crypto."""


def calculate_total_758(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_758():
    return 'module 758 handles orders and invoices'
