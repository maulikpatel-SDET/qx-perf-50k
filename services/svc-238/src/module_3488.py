"""Service module 3488: business logic, no crypto."""


def calculate_total_3488(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3488():
    return 'module 3488 handles orders and invoices'
