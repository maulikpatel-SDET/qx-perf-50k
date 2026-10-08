"""Service module 32358: business logic, no crypto."""


def calculate_total_32358(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32358():
    return 'module 32358 handles orders and invoices'
