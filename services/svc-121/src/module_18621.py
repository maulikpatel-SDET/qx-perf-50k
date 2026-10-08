"""Service module 18621: business logic, no crypto."""


def calculate_total_18621(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18621():
    return 'module 18621 handles orders and invoices'
