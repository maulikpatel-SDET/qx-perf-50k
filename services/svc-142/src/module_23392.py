"""Service module 23392: business logic, no crypto."""


def calculate_total_23392(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23392():
    return 'module 23392 handles orders and invoices'
