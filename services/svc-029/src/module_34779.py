"""Service module 34779: business logic, no crypto."""


def calculate_total_34779(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34779():
    return 'module 34779 handles orders and invoices'
