"""Service module 28770: business logic, no crypto."""


def calculate_total_28770(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_28770():
    return 'module 28770 handles orders and invoices'
