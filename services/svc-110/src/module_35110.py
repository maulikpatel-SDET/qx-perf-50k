"""Service module 35110: business logic, no crypto."""


def calculate_total_35110(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35110():
    return 'module 35110 handles orders and invoices'
