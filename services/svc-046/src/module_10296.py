"""Service module 10296: business logic, no crypto."""


def calculate_total_10296(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10296():
    return 'module 10296 handles orders and invoices'
