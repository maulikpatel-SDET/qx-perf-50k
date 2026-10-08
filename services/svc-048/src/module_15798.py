"""Service module 15798: business logic, no crypto."""


def calculate_total_15798(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15798():
    return 'module 15798 handles orders and invoices'
