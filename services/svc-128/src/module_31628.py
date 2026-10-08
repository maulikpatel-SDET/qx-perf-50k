"""Service module 31628: business logic, no crypto."""


def calculate_total_31628(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31628():
    return 'module 31628 handles orders and invoices'
