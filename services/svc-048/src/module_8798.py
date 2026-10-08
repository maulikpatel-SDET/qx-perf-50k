"""Service module 8798: business logic, no crypto."""


def calculate_total_8798(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8798():
    return 'module 8798 handles orders and invoices'
