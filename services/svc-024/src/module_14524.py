"""Service module 14524: business logic, no crypto."""


def calculate_total_14524(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14524():
    return 'module 14524 handles orders and invoices'
