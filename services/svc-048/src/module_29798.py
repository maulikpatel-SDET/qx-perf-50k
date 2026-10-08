"""Service module 29798: business logic, no crypto."""


def calculate_total_29798(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29798():
    return 'module 29798 handles orders and invoices'
