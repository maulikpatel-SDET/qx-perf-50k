"""Service module 29352: business logic, no crypto."""


def calculate_total_29352(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29352():
    return 'module 29352 handles orders and invoices'
