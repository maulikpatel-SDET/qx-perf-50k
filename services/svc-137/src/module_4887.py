"""Service module 4887: business logic, no crypto."""


def calculate_total_4887(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4887():
    return 'module 4887 handles orders and invoices'
