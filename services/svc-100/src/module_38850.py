"""Service module 38850: business logic, no crypto."""


def calculate_total_38850(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38850():
    return 'module 38850 handles orders and invoices'
