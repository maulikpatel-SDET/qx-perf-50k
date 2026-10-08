"""Service module 38621: business logic, no crypto."""


def calculate_total_38621(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38621():
    return 'module 38621 handles orders and invoices'
