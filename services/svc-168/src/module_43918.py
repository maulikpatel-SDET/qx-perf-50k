"""Service module 43918: business logic, no crypto."""


def calculate_total_43918(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_43918():
    return 'module 43918 handles orders and invoices'
