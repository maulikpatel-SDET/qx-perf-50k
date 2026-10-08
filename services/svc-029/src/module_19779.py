"""Service module 19779: business logic, no crypto."""


def calculate_total_19779(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19779():
    return 'module 19779 handles orders and invoices'
