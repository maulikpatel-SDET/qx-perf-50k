"""Service module 29135: business logic, no crypto."""


def calculate_total_29135(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29135():
    return 'module 29135 handles orders and invoices'
