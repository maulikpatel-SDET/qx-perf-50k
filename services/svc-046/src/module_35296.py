"""Service module 35296: business logic, no crypto."""


def calculate_total_35296(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35296():
    return 'module 35296 handles orders and invoices'
