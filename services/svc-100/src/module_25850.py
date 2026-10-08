"""Service module 25850: business logic, no crypto."""


def calculate_total_25850(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25850():
    return 'module 25850 handles orders and invoices'
