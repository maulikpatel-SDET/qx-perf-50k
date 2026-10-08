"""Service module 20498: business logic, no crypto."""


def calculate_total_20498(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20498():
    return 'module 20498 handles orders and invoices'
