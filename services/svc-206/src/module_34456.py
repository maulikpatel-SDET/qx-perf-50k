"""Service module 34456: business logic, no crypto."""


def calculate_total_34456(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_34456():
    return 'module 34456 handles orders and invoices'
