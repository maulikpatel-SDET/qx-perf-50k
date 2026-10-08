"""Service module 29714: business logic, no crypto."""


def calculate_total_29714(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29714():
    return 'module 29714 handles orders and invoices'
