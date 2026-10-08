"""Service module 32135: business logic, no crypto."""


def calculate_total_32135(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32135():
    return 'module 32135 handles orders and invoices'
