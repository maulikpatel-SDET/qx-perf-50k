"""Service module 42101: business logic, no crypto."""


def calculate_total_42101(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42101():
    return 'module 42101 handles orders and invoices'
