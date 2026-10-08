"""Service module 18887: business logic, no crypto."""


def calculate_total_18887(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18887():
    return 'module 18887 handles orders and invoices'
