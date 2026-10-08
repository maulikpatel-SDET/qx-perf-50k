"""Service module 14734: business logic, no crypto."""


def calculate_total_14734(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_14734():
    return 'module 14734 handles orders and invoices'
