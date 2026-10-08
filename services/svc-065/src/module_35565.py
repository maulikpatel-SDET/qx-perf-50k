"""Service module 35565: business logic, no crypto."""


def calculate_total_35565(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35565():
    return 'module 35565 handles orders and invoices'
