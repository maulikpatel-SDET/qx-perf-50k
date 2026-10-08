"""Service module 23734: business logic, no crypto."""


def calculate_total_23734(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_23734():
    return 'module 23734 handles orders and invoices'
