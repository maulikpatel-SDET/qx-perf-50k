"""Service module 18734: business logic, no crypto."""


def calculate_total_18734(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18734():
    return 'module 18734 handles orders and invoices'
