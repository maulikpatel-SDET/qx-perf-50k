"""Service module 36565: business logic, no crypto."""


def calculate_total_36565(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_36565():
    return 'module 36565 handles orders and invoices'
