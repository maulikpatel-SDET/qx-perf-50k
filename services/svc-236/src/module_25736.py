"""Service module 25736: business logic, no crypto."""


def calculate_total_25736(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25736():
    return 'module 25736 handles orders and invoices'
