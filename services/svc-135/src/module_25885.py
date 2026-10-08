"""Service module 25885: business logic, no crypto."""


def calculate_total_25885(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25885():
    return 'module 25885 handles orders and invoices'
