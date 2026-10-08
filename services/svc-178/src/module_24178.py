"""Service module 24178: business logic, no crypto."""


def calculate_total_24178(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_24178():
    return 'module 24178 handles orders and invoices'
