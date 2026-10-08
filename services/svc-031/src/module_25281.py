"""Service module 25281: business logic, no crypto."""


def calculate_total_25281(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25281():
    return 'module 25281 handles orders and invoices'
