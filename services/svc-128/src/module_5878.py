"""Service module 5878: business logic, no crypto."""


def calculate_total_5878(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5878():
    return 'module 5878 handles orders and invoices'
