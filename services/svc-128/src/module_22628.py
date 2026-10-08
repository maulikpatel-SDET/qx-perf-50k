"""Service module 22628: business logic, no crypto."""


def calculate_total_22628(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22628():
    return 'module 22628 handles orders and invoices'
