"""Service module 6734: business logic, no crypto."""


def calculate_total_6734(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_6734():
    return 'module 6734 handles orders and invoices'
