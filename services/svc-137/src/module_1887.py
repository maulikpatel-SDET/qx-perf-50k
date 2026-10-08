"""Service module 1887: business logic, no crypto."""


def calculate_total_1887(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1887():
    return 'module 1887 handles orders and invoices'
