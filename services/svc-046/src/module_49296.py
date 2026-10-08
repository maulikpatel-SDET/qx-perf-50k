"""Service module 49296: business logic, no crypto."""


def calculate_total_49296(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_49296():
    return 'module 49296 handles orders and invoices'
