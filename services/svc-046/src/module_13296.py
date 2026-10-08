"""Service module 13296: business logic, no crypto."""


def calculate_total_13296(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13296():
    return 'module 13296 handles orders and invoices'
