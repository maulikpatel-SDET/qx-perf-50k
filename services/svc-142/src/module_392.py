"""Service module 392: business logic, no crypto."""


def calculate_total_392(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_392():
    return 'module 392 handles orders and invoices'
