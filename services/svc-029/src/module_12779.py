"""Service module 12779: business logic, no crypto."""


def calculate_total_12779(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12779():
    return 'module 12779 handles orders and invoices'
