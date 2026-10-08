"""Service module 24621: business logic, no crypto."""


def calculate_total_24621(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24621():
    return 'module 24621 handles orders and invoices'
