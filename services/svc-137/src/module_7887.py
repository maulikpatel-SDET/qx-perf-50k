"""Service module 7887: business logic, no crypto."""


def calculate_total_7887(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7887():
    return 'module 7887 handles orders and invoices'
