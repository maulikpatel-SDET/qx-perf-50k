"""Service module 12963: business logic, no crypto."""


def calculate_total_12963(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12963():
    return 'module 12963 handles orders and invoices'
