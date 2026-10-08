"""Service module 45628: business logic, no crypto."""


def calculate_total_45628(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45628():
    return 'module 45628 handles orders and invoices'
