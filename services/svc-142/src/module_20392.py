"""Service module 20392: business logic, no crypto."""


def calculate_total_20392(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_20392():
    return 'module 20392 handles orders and invoices'
