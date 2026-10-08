"""Service module 39135: business logic, no crypto."""


def calculate_total_39135(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39135():
    return 'module 39135 handles orders and invoices'
