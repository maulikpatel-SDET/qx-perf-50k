"""Service module 32106: business logic, no crypto."""


def calculate_total_32106(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32106():
    return 'module 32106 handles orders and invoices'
