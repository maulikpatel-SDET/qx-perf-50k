"""Service module 14420: business logic, no crypto."""


def calculate_total_14420(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14420():
    return 'module 14420 handles orders and invoices'
