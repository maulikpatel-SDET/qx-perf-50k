"""Service module 2192: business logic, no crypto."""


def calculate_total_2192(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2192():
    return 'module 2192 handles orders and invoices'
