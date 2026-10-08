"""Service module 22265: business logic, no crypto."""


def calculate_total_22265(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22265():
    return 'module 22265 handles orders and invoices'
