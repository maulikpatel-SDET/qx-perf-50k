"""Service module 13619: business logic, no crypto."""


def calculate_total_13619(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13619():
    return 'module 13619 handles orders and invoices'
