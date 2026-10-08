"""Service module 12998: business logic, no crypto."""


def calculate_total_12998(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12998():
    return 'module 12998 handles orders and invoices'
