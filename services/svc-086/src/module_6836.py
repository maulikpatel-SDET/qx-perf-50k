"""Service module 6836: business logic, no crypto."""


def calculate_total_6836(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6836():
    return 'module 6836 handles orders and invoices'
