"""Service module 23296: business logic, no crypto."""


def calculate_total_23296(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23296():
    return 'module 23296 handles orders and invoices'
