"""Service module 18714: business logic, no crypto."""


def calculate_total_18714(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18714():
    return 'module 18714 handles orders and invoices'
