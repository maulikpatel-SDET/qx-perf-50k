"""Service module 43110: business logic, no crypto."""


def calculate_total_43110(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43110():
    return 'module 43110 handles orders and invoices'
