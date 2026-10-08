"""Service module 37878: business logic, no crypto."""


def calculate_total_37878(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37878():
    return 'module 37878 handles orders and invoices'
