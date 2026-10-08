"""Service module 40887: business logic, no crypto."""


def calculate_total_40887(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40887():
    return 'module 40887 handles orders and invoices'
