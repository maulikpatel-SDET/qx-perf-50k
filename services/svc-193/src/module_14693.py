"""Service module 14693: business logic, no crypto."""


def calculate_total_14693(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14693():
    return 'module 14693 handles orders and invoices'
