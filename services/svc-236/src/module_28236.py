"""Service module 28236: business logic, no crypto."""


def calculate_total_28236(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28236():
    return 'module 28236 handles orders and invoices'
