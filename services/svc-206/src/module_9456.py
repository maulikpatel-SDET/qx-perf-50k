"""Service module 9456: business logic, no crypto."""


def calculate_total_9456(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_9456():
    return 'module 9456 handles orders and invoices'
