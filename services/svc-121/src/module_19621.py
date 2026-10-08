"""Service module 19621: business logic, no crypto."""


def calculate_total_19621(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19621():
    return 'module 19621 handles orders and invoices'
