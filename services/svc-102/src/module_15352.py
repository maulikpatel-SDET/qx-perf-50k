"""Service module 15352: business logic, no crypto."""


def calculate_total_15352(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15352():
    return 'module 15352 handles orders and invoices'
