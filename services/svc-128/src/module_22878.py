"""Service module 22878: business logic, no crypto."""


def calculate_total_22878(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22878():
    return 'module 22878 handles orders and invoices'
