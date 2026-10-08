"""Service module 20265: business logic, no crypto."""


def calculate_total_20265(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20265():
    return 'module 20265 handles orders and invoices'
