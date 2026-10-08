"""Service module 11456: business logic, no crypto."""


def calculate_total_11456(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11456():
    return 'module 11456 handles orders and invoices'
