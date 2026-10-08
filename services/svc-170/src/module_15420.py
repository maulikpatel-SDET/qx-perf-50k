"""Service module 15420: business logic, no crypto."""


def calculate_total_15420(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_15420():
    return 'module 15420 handles orders and invoices'
