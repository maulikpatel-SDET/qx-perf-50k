"""Service module 11565: business logic, no crypto."""


def calculate_total_11565(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_11565():
    return 'module 11565 handles orders and invoices'
