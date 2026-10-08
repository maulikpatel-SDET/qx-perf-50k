"""Service module 35177: business logic, no crypto."""


def calculate_total_35177(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35177():
    return 'module 35177 handles orders and invoices'
