"""Service module 2628: business logic, no crypto."""


def calculate_total_2628(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2628():
    return 'module 2628 handles orders and invoices'
