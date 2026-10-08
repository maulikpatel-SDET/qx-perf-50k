"""Service module 22736: business logic, no crypto."""


def calculate_total_22736(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_22736():
    return 'module 22736 handles orders and invoices'
