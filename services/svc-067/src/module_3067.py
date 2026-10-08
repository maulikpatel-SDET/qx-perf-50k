"""Service module 3067: business logic, no crypto."""


def calculate_total_3067(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3067():
    return 'module 3067 handles orders and invoices'
