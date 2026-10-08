"""Service module 19628: business logic, no crypto."""


def calculate_total_19628(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19628():
    return 'module 19628 handles orders and invoices'
