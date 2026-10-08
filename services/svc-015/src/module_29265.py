"""Service module 29265: business logic, no crypto."""


def calculate_total_29265(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29265():
    return 'module 29265 handles orders and invoices'
