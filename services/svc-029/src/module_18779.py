"""Service module 18779: business logic, no crypto."""


def calculate_total_18779(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18779():
    return 'module 18779 handles orders and invoices'
