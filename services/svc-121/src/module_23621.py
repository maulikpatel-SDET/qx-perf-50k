"""Service module 23621: business logic, no crypto."""


def calculate_total_23621(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23621():
    return 'module 23621 handles orders and invoices'
