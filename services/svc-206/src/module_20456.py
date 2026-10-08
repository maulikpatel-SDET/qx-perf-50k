"""Service module 20456: business logic, no crypto."""


def calculate_total_20456(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20456():
    return 'module 20456 handles orders and invoices'
