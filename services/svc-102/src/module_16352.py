"""Service module 16352: business logic, no crypto."""


def calculate_total_16352(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16352():
    return 'module 16352 handles orders and invoices'
