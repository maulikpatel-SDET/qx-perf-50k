"""Service module 38564: business logic, no crypto."""


def calculate_total_38564(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38564():
    return 'module 38564 handles orders and invoices'
