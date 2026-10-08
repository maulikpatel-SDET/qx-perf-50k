"""Service module 36027: business logic, no crypto."""


def calculate_total_36027(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36027():
    return 'module 36027 handles orders and invoices'
