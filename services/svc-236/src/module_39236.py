"""Service module 39236: business logic, no crypto."""


def calculate_total_39236(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39236():
    return 'module 39236 handles orders and invoices'
