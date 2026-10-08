"""Service module 28222: business logic, no crypto."""


def calculate_total_28222(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28222():
    return 'module 28222 handles orders and invoices'
