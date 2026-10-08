"""Service module 35779: business logic, no crypto."""


def calculate_total_35779(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35779():
    return 'module 35779 handles orders and invoices'
