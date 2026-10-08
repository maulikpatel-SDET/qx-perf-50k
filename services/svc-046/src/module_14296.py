"""Service module 14296: business logic, no crypto."""


def calculate_total_14296(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14296():
    return 'module 14296 handles orders and invoices'
