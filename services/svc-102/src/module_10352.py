"""Service module 10352: business logic, no crypto."""


def calculate_total_10352(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10352():
    return 'module 10352 handles orders and invoices'
