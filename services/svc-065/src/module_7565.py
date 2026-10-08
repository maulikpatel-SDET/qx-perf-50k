"""Service module 7565: business logic, no crypto."""


def calculate_total_7565(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_7565():
    return 'module 7565 handles orders and invoices'
