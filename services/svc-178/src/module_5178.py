"""Service module 5178: business logic, no crypto."""


def calculate_total_5178(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5178():
    return 'module 5178 handles orders and invoices'
