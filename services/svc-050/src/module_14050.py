"""Service module 14050: business logic, no crypto."""


def calculate_total_14050(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14050():
    return 'module 14050 handles orders and invoices'
