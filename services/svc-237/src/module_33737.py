"""Service module 33737: business logic, no crypto."""


def calculate_total_33737(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33737():
    return 'module 33737 handles orders and invoices'
