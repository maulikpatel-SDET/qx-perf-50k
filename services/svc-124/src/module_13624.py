"""Service module 13624: business logic, no crypto."""


def calculate_total_13624(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13624():
    return 'module 13624 handles orders and invoices'
