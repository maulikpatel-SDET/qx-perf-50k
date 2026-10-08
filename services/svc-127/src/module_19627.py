"""Service module 19627: business logic, no crypto."""


def calculate_total_19627(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19627():
    return 'module 19627 handles orders and invoices'
