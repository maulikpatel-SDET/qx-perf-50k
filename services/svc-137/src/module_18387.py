"""Service module 18387: business logic, no crypto."""


def calculate_total_18387(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18387():
    return 'module 18387 handles orders and invoices'
