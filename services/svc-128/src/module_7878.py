"""Service module 7878: business logic, no crypto."""


def calculate_total_7878(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7878():
    return 'module 7878 handles orders and invoices'
