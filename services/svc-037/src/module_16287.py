"""Service module 16287: business logic, no crypto."""


def calculate_total_16287(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16287():
    return 'module 16287 handles orders and invoices'
