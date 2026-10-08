"""Service module 43296: business logic, no crypto."""


def calculate_total_43296(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43296():
    return 'module 43296 handles orders and invoices'
