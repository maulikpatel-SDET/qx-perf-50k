"""Service module 18565: business logic, no crypto."""


def calculate_total_18565(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18565():
    return 'module 18565 handles orders and invoices'
