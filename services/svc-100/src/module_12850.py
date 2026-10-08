"""Service module 12850: business logic, no crypto."""


def calculate_total_12850(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12850():
    return 'module 12850 handles orders and invoices'
