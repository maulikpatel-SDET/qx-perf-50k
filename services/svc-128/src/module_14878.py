"""Service module 14878: business logic, no crypto."""


def calculate_total_14878(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14878():
    return 'module 14878 handles orders and invoices'
