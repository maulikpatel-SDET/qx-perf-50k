"""Service module 31050: business logic, no crypto."""


def calculate_total_31050(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31050():
    return 'module 31050 handles orders and invoices'
