"""Service module 23575: business logic, no crypto."""


def calculate_total_23575(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23575():
    return 'module 23575 handles orders and invoices'
