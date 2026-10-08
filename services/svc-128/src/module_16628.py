"""Service module 16628: business logic, no crypto."""


def calculate_total_16628(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_16628():
    return 'module 16628 handles orders and invoices'
