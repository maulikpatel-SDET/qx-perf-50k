"""Service module 32178: business logic, no crypto."""


def calculate_total_32178(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_32178():
    return 'module 32178 handles orders and invoices'
