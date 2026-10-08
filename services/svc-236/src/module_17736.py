"""Service module 17736: business logic, no crypto."""


def calculate_total_17736(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17736():
    return 'module 17736 handles orders and invoices'
