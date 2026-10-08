"""Service module 2654: business logic, no crypto."""


def calculate_total_2654(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2654():
    return 'module 2654 handles orders and invoices'
