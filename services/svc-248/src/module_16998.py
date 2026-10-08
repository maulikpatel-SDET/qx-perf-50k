"""Service module 16998: business logic, no crypto."""


def calculate_total_16998(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16998():
    return 'module 16998 handles orders and invoices'
