"""Service module 14456: business logic, no crypto."""


def calculate_total_14456(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14456():
    return 'module 14456 handles orders and invoices'
