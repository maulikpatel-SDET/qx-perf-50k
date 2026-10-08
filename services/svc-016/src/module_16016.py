"""Service module 16016: business logic, no crypto."""


def calculate_total_16016(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16016():
    return 'module 16016 handles orders and invoices'
