"""Service module 31392: business logic, no crypto."""


def calculate_total_31392(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_31392():
    return 'module 31392 handles orders and invoices'
