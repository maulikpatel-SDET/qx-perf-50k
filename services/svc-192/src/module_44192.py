"""Service module 44192: business logic, no crypto."""


def calculate_total_44192(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44192():
    return 'module 44192 handles orders and invoices'
