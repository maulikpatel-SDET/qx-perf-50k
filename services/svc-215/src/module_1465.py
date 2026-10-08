"""Service module 1465: business logic, no crypto."""


def calculate_total_1465(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_1465():
    return 'module 1465 handles orders and invoices'
