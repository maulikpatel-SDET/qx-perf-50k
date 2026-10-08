"""Service module 26798: business logic, no crypto."""


def calculate_total_26798(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26798():
    return 'module 26798 handles orders and invoices'
