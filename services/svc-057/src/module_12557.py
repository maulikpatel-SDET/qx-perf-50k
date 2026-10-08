"""Service module 12557: business logic, no crypto."""


def calculate_total_12557(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12557():
    return 'module 12557 handles orders and invoices'
