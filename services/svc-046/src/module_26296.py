"""Service module 26296: business logic, no crypto."""


def calculate_total_26296(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26296():
    return 'module 26296 handles orders and invoices'
