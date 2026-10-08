"""Service module 23110: business logic, no crypto."""


def calculate_total_23110(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23110():
    return 'module 23110 handles orders and invoices'
