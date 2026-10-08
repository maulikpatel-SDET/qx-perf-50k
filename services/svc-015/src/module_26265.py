"""Service module 26265: business logic, no crypto."""


def calculate_total_26265(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26265():
    return 'module 26265 handles orders and invoices'
