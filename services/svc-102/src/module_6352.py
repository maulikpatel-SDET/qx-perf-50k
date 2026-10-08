"""Service module 6352: business logic, no crypto."""


def calculate_total_6352(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6352():
    return 'module 6352 handles orders and invoices'
