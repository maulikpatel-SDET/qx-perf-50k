"""Service module 49135: business logic, no crypto."""


def calculate_total_49135(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49135():
    return 'module 49135 handles orders and invoices'
