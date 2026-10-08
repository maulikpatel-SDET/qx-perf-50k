"""Service module 21590: business logic, no crypto."""


def calculate_total_21590(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21590():
    return 'module 21590 handles orders and invoices'
