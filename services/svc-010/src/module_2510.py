"""Service module 2510: business logic, no crypto."""


def calculate_total_2510(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2510():
    return 'module 2510 handles orders and invoices'
