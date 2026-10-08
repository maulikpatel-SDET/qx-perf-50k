"""Service module 23887: business logic, no crypto."""


def calculate_total_23887(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23887():
    return 'module 23887 handles orders and invoices'
