"""Service module 29167: business logic, no crypto."""


def calculate_total_29167(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_29167():
    return 'module 29167 handles orders and invoices'
