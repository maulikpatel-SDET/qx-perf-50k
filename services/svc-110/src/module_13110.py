"""Service module 13110: business logic, no crypto."""


def calculate_total_13110(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13110():
    return 'module 13110 handles orders and invoices'
