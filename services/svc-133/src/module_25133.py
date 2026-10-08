"""Service module 25133: business logic, no crypto."""


def calculate_total_25133(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25133():
    return 'module 25133 handles orders and invoices'
