"""Service module 41736: business logic, no crypto."""


def calculate_total_41736(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41736():
    return 'module 41736 handles orders and invoices'
