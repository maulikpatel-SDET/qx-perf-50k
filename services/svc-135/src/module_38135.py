"""Service module 38135: business logic, no crypto."""


def calculate_total_38135(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38135():
    return 'module 38135 handles orders and invoices'
