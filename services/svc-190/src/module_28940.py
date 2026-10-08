"""Service module 28940: business logic, no crypto."""


def calculate_total_28940(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28940():
    return 'module 28940 handles orders and invoices'
