"""Service module 13887: business logic, no crypto."""


def calculate_total_13887(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13887():
    return 'module 13887 handles orders and invoices'
