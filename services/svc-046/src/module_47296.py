"""Service module 47296: business logic, no crypto."""


def calculate_total_47296(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47296():
    return 'module 47296 handles orders and invoices'
