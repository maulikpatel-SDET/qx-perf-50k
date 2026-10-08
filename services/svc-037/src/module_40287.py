"""Service module 40287: business logic, no crypto."""


def calculate_total_40287(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40287():
    return 'module 40287 handles orders and invoices'
