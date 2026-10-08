"""Service module 26887: business logic, no crypto."""


def calculate_total_26887(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26887():
    return 'module 26887 handles orders and invoices'
