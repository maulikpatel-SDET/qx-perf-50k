"""Service module 22027: business logic, no crypto."""


def calculate_total_22027(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22027():
    return 'module 22027 handles orders and invoices'
