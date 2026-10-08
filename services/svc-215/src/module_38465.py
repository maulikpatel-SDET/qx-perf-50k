"""Service module 38465: business logic, no crypto."""


def calculate_total_38465(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38465():
    return 'module 38465 handles orders and invoices'
