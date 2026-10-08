"""Service module 41178: business logic, no crypto."""


def calculate_total_41178(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41178():
    return 'module 41178 handles orders and invoices'
