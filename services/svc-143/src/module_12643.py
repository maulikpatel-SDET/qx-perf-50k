"""Service module 12643: business logic, no crypto."""


def calculate_total_12643(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12643():
    return 'module 12643 handles orders and invoices'
