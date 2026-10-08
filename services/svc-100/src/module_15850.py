"""Service module 15850: business logic, no crypto."""


def calculate_total_15850(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15850():
    return 'module 15850 handles orders and invoices'
