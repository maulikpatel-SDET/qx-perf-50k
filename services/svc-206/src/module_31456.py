"""Service module 31456: business logic, no crypto."""


def calculate_total_31456(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31456():
    return 'module 31456 handles orders and invoices'
