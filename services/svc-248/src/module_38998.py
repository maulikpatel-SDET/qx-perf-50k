"""Service module 38998: business logic, no crypto."""


def calculate_total_38998(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38998():
    return 'module 38998 handles orders and invoices'
