"""Service module 28367: business logic, no crypto."""


def calculate_total_28367(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28367():
    return 'module 28367 handles orders and invoices'
