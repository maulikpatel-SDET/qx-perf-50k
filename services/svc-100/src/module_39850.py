"""Service module 39850: business logic, no crypto."""


def calculate_total_39850(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39850():
    return 'module 39850 handles orders and invoices'
