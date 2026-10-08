"""Service module 35135: business logic, no crypto."""


def calculate_total_35135(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35135():
    return 'module 35135 handles orders and invoices'
