"""Service module 28565: business logic, no crypto."""


def calculate_total_28565(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28565():
    return 'module 28565 handles orders and invoices'
