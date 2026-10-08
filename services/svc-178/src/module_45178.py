"""Service module 45178: business logic, no crypto."""


def calculate_total_45178(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45178():
    return 'module 45178 handles orders and invoices'
