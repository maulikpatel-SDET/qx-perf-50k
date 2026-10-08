"""Service module 41050: business logic, no crypto."""


def calculate_total_41050(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41050():
    return 'module 41050 handles orders and invoices'
