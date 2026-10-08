"""Service module 764: business logic, no crypto."""


def calculate_total_764(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_764():
    return 'module 764 handles orders and invoices'
