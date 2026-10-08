"""Service module 20158: business logic, no crypto."""


def calculate_total_20158(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20158():
    return 'module 20158 handles orders and invoices'
