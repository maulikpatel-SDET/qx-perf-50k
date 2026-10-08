"""Service module 21352: business logic, no crypto."""


def calculate_total_21352(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21352():
    return 'module 21352 handles orders and invoices'
