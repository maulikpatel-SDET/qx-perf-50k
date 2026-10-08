"""Service module 26416: business logic, no crypto."""


def calculate_total_26416(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26416():
    return 'module 26416 handles orders and invoices'
