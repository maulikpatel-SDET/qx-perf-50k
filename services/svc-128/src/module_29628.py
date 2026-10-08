"""Service module 29628: business logic, no crypto."""


def calculate_total_29628(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29628():
    return 'module 29628 handles orders and invoices'
