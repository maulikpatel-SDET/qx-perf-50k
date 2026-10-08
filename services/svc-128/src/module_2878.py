"""Service module 2878: business logic, no crypto."""


def calculate_total_2878(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2878():
    return 'module 2878 handles orders and invoices'
