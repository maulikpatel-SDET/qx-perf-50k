"""Service module 23439: business logic, no crypto."""


def calculate_total_23439(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23439():
    return 'module 23439 handles orders and invoices'
