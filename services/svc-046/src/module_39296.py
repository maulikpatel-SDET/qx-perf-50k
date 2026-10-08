"""Service module 39296: business logic, no crypto."""


def calculate_total_39296(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39296():
    return 'module 39296 handles orders and invoices'
