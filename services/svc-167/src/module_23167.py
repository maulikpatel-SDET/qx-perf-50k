"""Service module 23167: business logic, no crypto."""


def calculate_total_23167(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23167():
    return 'module 23167 handles orders and invoices'
