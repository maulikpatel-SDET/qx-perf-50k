"""Service module 31379: business logic, no crypto."""


def calculate_total_31379(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31379():
    return 'module 31379 handles orders and invoices'
