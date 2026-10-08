"""Service module 36135: business logic, no crypto."""


def calculate_total_36135(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36135():
    return 'module 36135 handles orders and invoices'
