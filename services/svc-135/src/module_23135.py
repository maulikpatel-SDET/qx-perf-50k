"""Service module 23135: business logic, no crypto."""


def calculate_total_23135(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23135():
    return 'module 23135 handles orders and invoices'
