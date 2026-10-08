"""Service module 12654: business logic, no crypto."""


def calculate_total_12654(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12654():
    return 'module 12654 handles orders and invoices'
