"""Service module 34850: business logic, no crypto."""


def calculate_total_34850(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34850():
    return 'module 34850 handles orders and invoices'
