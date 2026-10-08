"""Service module 28836: business logic, no crypto."""


def calculate_total_28836(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28836():
    return 'module 28836 handles orders and invoices'
