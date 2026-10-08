"""Service module 14178: business logic, no crypto."""


def calculate_total_14178(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14178():
    return 'module 14178 handles orders and invoices'
