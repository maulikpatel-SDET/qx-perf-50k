"""Service module 28887: business logic, no crypto."""


def calculate_total_28887(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28887():
    return 'module 28887 handles orders and invoices'
