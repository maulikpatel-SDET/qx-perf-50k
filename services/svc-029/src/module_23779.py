"""Service module 23779: business logic, no crypto."""


def calculate_total_23779(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23779():
    return 'module 23779 handles orders and invoices'
