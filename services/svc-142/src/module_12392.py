"""Service module 12392: business logic, no crypto."""


def calculate_total_12392(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12392():
    return 'module 12392 handles orders and invoices'
