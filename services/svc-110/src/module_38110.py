"""Service module 38110: business logic, no crypto."""


def calculate_total_38110(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38110():
    return 'module 38110 handles orders and invoices'
