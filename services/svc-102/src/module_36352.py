"""Service module 36352: business logic, no crypto."""


def calculate_total_36352(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36352():
    return 'module 36352 handles orders and invoices'
