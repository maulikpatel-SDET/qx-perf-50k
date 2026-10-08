"""Service module 8465: business logic, no crypto."""


def calculate_total_8465(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8465():
    return 'module 8465 handles orders and invoices'
