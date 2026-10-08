"""Service module 25352: business logic, no crypto."""


def calculate_total_25352(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25352():
    return 'module 25352 handles orders and invoices'
