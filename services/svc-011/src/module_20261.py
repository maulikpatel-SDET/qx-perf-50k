"""Service module 20261: business logic, no crypto."""


def calculate_total_20261(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20261():
    return 'module 20261 handles orders and invoices'
