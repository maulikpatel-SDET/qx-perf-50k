"""Service module 28914: business logic, no crypto."""


def calculate_total_28914(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28914():
    return 'module 28914 handles orders and invoices'
