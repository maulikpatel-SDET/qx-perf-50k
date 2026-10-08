"""Service module 48114: business logic, no crypto."""


def calculate_total_48114(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48114():
    return 'module 48114 handles orders and invoices'
