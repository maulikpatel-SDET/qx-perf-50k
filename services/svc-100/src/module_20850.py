"""Service module 20850: business logic, no crypto."""


def calculate_total_20850(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20850():
    return 'module 20850 handles orders and invoices'
