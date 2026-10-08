"""Service module 39779: business logic, no crypto."""


def calculate_total_39779(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39779():
    return 'module 39779 handles orders and invoices'
