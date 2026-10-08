"""Service module 9887: business logic, no crypto."""


def calculate_total_9887(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9887():
    return 'module 9887 handles orders and invoices'
