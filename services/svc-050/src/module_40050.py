"""Service module 40050: business logic, no crypto."""


def calculate_total_40050(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40050():
    return 'module 40050 handles orders and invoices'
