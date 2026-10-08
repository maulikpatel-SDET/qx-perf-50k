"""Service module 21734: business logic, no crypto."""


def calculate_total_21734(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21734():
    return 'module 21734 handles orders and invoices'
