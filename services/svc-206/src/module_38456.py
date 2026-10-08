"""Service module 38456: business logic, no crypto."""


def calculate_total_38456(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38456():
    return 'module 38456 handles orders and invoices'
