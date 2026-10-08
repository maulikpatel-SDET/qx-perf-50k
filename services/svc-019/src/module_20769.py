"""Service module 20769: business logic, no crypto."""


def calculate_total_20769(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20769():
    return 'module 20769 handles orders and invoices'
