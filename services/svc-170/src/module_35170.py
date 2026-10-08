"""Service module 35170: business logic, no crypto."""


def calculate_total_35170(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35170():
    return 'module 35170 handles orders and invoices'
