"""Service module 13470: business logic, no crypto."""


def calculate_total_13470(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_13470():
    return 'module 13470 handles orders and invoices'
