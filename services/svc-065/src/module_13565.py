"""Service module 13565: business logic, no crypto."""


def calculate_total_13565(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13565():
    return 'module 13565 handles orders and invoices'
