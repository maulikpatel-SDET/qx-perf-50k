"""Service module 30178: business logic, no crypto."""


def calculate_total_30178(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30178():
    return 'module 30178 handles orders and invoices'
