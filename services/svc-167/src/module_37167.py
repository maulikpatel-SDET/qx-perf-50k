"""Service module 37167: business logic, no crypto."""


def calculate_total_37167(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37167():
    return 'module 37167 handles orders and invoices'
