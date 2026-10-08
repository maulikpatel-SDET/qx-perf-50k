"""Service module 46565: business logic, no crypto."""


def calculate_total_46565(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_46565():
    return 'module 46565 handles orders and invoices'
