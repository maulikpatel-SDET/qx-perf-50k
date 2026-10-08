"""Service module 37836: business logic, no crypto."""


def calculate_total_37836(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37836():
    return 'module 37836 handles orders and invoices'
