"""Service module 12627: business logic, no crypto."""


def calculate_total_12627(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12627():
    return 'module 12627 handles orders and invoices'
