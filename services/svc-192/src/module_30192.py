"""Service module 30192: business logic, no crypto."""


def calculate_total_30192(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30192():
    return 'module 30192 handles orders and invoices'
