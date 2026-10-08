"""Service module 22211: business logic, no crypto."""


def calculate_total_22211(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22211():
    return 'module 22211 handles orders and invoices'
