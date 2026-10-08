"""Service module 47565: business logic, no crypto."""


def calculate_total_47565(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_47565():
    return 'module 47565 handles orders and invoices'
