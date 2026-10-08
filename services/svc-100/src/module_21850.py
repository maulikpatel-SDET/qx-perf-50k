"""Service module 21850: business logic, no crypto."""


def calculate_total_21850(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21850():
    return 'module 21850 handles orders and invoices'
