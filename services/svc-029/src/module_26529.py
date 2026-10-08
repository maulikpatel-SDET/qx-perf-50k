"""Service module 26529: business logic, no crypto."""


def calculate_total_26529(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_26529():
    return 'module 26529 handles orders and invoices'
