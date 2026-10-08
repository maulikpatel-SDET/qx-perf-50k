"""Service module 22654: business logic, no crypto."""


def calculate_total_22654(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22654():
    return 'module 22654 handles orders and invoices'
