"""Service module 34714: business logic, no crypto."""


def calculate_total_34714(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34714():
    return 'module 34714 handles orders and invoices'
