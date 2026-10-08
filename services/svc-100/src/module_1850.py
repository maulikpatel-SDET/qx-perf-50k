"""Service module 1850: business logic, no crypto."""


def calculate_total_1850(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1850():
    return 'module 1850 handles orders and invoices'
