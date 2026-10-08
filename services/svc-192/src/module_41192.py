"""Service module 41192: business logic, no crypto."""


def calculate_total_41192(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41192():
    return 'module 41192 handles orders and invoices'
