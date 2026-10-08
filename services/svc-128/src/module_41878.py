"""Service module 41878: business logic, no crypto."""


def calculate_total_41878(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41878():
    return 'module 41878 handles orders and invoices'
