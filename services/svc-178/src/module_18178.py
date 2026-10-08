"""Service module 18178: business logic, no crypto."""


def calculate_total_18178(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18178():
    return 'module 18178 handles orders and invoices'
