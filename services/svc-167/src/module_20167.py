"""Service module 20167: business logic, no crypto."""


def calculate_total_20167(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20167():
    return 'module 20167 handles orders and invoices'
