"""Service module 16878: business logic, no crypto."""


def calculate_total_16878(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16878():
    return 'module 16878 handles orders and invoices'
