"""Service module 23628: business logic, no crypto."""


def calculate_total_23628(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23628():
    return 'module 23628 handles orders and invoices'
