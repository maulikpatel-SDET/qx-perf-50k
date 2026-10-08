"""Service module 13998: business logic, no crypto."""


def calculate_total_13998(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13998():
    return 'module 13998 handles orders and invoices'
