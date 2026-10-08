"""Service module 35850: business logic, no crypto."""


def calculate_total_35850(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35850():
    return 'module 35850 handles orders and invoices'
