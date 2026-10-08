"""Service module 29296: business logic, no crypto."""


def calculate_total_29296(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29296():
    return 'module 29296 handles orders and invoices'
