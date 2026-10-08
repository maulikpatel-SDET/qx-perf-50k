"""Service module 23456: business logic, no crypto."""


def calculate_total_23456(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23456():
    return 'module 23456 handles orders and invoices'
