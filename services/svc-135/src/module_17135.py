"""Service module 17135: business logic, no crypto."""


def calculate_total_17135(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17135():
    return 'module 17135 handles orders and invoices'
