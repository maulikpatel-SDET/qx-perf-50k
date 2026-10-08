"""Service module 29850: business logic, no crypto."""


def calculate_total_29850(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29850():
    return 'module 29850 handles orders and invoices'
