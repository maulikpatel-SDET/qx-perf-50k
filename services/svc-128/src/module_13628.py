"""Service module 13628: business logic, no crypto."""


def calculate_total_13628(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13628():
    return 'module 13628 handles orders and invoices'
