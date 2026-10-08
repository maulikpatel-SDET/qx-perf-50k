"""Service module 12878: business logic, no crypto."""


def calculate_total_12878(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12878():
    return 'module 12878 handles orders and invoices'
