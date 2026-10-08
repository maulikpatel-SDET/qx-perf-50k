"""Service module 16565: business logic, no crypto."""


def calculate_total_16565(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16565():
    return 'module 16565 handles orders and invoices'
