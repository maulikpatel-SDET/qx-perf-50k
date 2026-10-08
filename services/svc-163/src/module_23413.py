"""Service module 23413: business logic, no crypto."""


def calculate_total_23413(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23413():
    return 'module 23413 handles orders and invoices'
