"""Service module 40377: business logic, no crypto."""


def calculate_total_40377(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40377():
    return 'module 40377 handles orders and invoices'
