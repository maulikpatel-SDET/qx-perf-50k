"""Service module 11798: business logic, no crypto."""


def calculate_total_11798(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11798():
    return 'module 11798 handles orders and invoices'
