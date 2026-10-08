"""Service module 39557: business logic, no crypto."""


def calculate_total_39557(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39557():
    return 'module 39557 handles orders and invoices'
