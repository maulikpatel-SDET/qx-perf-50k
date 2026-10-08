"""Service module 38050: business logic, no crypto."""


def calculate_total_38050(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38050():
    return 'module 38050 handles orders and invoices'
