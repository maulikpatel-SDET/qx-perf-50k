"""Service module 43749: business logic, no crypto."""


def calculate_total_43749(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43749():
    return 'module 43749 handles orders and invoices'
