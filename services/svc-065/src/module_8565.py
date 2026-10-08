"""Service module 8565: business logic, no crypto."""


def calculate_total_8565(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_8565():
    return 'module 8565 handles orders and invoices'
