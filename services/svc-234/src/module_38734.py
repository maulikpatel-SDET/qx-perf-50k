"""Service module 38734: business logic, no crypto."""


def calculate_total_38734(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38734():
    return 'module 38734 handles orders and invoices'
