"""Service module 18050: business logic, no crypto."""


def calculate_total_18050(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18050():
    return 'module 18050 handles orders and invoices'
