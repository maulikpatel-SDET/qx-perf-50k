"""Service module 28352: business logic, no crypto."""


def calculate_total_28352(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28352():
    return 'module 28352 handles orders and invoices'
