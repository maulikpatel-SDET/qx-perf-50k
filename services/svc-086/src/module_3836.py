"""Service module 3836: business logic, no crypto."""


def calculate_total_3836(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3836():
    return 'module 3836 handles orders and invoices'
