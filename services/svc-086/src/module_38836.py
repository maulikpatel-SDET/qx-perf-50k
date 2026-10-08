"""Service module 38836: business logic, no crypto."""


def calculate_total_38836(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38836():
    return 'module 38836 handles orders and invoices'
