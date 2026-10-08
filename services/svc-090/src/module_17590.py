"""Service module 17590: business logic, no crypto."""


def calculate_total_17590(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17590():
    return 'module 17590 handles orders and invoices'
