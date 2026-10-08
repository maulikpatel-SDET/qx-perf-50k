"""Service module 35628: business logic, no crypto."""


def calculate_total_35628(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35628():
    return 'module 35628 handles orders and invoices'
