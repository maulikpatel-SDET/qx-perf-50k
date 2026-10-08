"""Service module 11135: business logic, no crypto."""


def calculate_total_11135(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11135():
    return 'module 11135 handles orders and invoices'
