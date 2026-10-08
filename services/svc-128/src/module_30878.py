"""Service module 30878: business logic, no crypto."""


def calculate_total_30878(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30878():
    return 'module 30878 handles orders and invoices'
