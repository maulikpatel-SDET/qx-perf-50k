"""Service module 6878: business logic, no crypto."""


def calculate_total_6878(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6878():
    return 'module 6878 handles orders and invoices'
