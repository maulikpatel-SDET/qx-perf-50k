"""Service module 12420: business logic, no crypto."""


def calculate_total_12420(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_12420():
    return 'module 12420 handles orders and invoices'
