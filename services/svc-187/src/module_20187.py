"""Service module 20187: business logic, no crypto."""


def calculate_total_20187(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20187():
    return 'module 20187 handles orders and invoices'
