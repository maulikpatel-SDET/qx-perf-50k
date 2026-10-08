"""Service module 42621: business logic, no crypto."""


def calculate_total_42621(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42621():
    return 'module 42621 handles orders and invoices'
