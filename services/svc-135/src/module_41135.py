"""Service module 41135: business logic, no crypto."""


def calculate_total_41135(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41135():
    return 'module 41135 handles orders and invoices'
