"""Service module 31931: business logic, no crypto."""


def calculate_total_31931(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31931():
    return 'module 31931 handles orders and invoices'
