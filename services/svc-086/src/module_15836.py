"""Service module 15836: business logic, no crypto."""


def calculate_total_15836(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15836():
    return 'module 15836 handles orders and invoices'
