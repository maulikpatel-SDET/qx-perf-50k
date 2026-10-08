"""Service module 48178: business logic, no crypto."""


def calculate_total_48178(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_48178():
    return 'module 48178 handles orders and invoices'
