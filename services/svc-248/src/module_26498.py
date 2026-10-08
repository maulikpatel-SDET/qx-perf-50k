"""Service module 26498: business logic, no crypto."""


def calculate_total_26498(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26498():
    return 'module 26498 handles orders and invoices'
