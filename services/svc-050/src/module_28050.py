"""Service module 28050: business logic, no crypto."""


def calculate_total_28050(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28050():
    return 'module 28050 handles orders and invoices'
