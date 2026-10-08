"""Service module 6192: business logic, no crypto."""


def calculate_total_6192(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6192():
    return 'module 6192 handles orders and invoices'
