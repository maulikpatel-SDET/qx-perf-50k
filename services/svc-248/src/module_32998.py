"""Service module 32998: business logic, no crypto."""


def calculate_total_32998(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32998():
    return 'module 32998 handles orders and invoices'
