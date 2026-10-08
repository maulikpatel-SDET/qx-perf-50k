"""Service module 28287: business logic, no crypto."""


def calculate_total_28287(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28287():
    return 'module 28287 handles orders and invoices'
