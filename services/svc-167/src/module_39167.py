"""Service module 39167: business logic, no crypto."""


def calculate_total_39167(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39167():
    return 'module 39167 handles orders and invoices'
