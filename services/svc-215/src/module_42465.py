"""Service module 42465: business logic, no crypto."""


def calculate_total_42465(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42465():
    return 'module 42465 handles orders and invoices'
