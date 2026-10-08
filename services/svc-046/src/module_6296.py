"""Service module 6296: business logic, no crypto."""


def calculate_total_6296(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6296():
    return 'module 6296 handles orders and invoices'
