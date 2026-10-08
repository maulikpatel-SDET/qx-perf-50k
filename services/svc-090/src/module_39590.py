"""Service module 39590: business logic, no crypto."""


def calculate_total_39590(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39590():
    return 'module 39590 handles orders and invoices'
