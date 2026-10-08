"""Service module 26110: business logic, no crypto."""


def calculate_total_26110(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26110():
    return 'module 26110 handles orders and invoices'
