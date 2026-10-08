"""Service module 12624: business logic, no crypto."""


def calculate_total_12624(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12624():
    return 'module 12624 handles orders and invoices'
