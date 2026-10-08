"""Service module 47850: business logic, no crypto."""


def calculate_total_47850(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47850():
    return 'module 47850 handles orders and invoices'
