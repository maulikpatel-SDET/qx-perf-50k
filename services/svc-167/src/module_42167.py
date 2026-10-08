"""Service module 42167: business logic, no crypto."""


def calculate_total_42167(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_42167():
    return 'module 42167 handles orders and invoices'
