"""Service module 44850: business logic, no crypto."""


def calculate_total_44850(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44850():
    return 'module 44850 handles orders and invoices'
