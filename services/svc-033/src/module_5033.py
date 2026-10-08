"""Service module 5033: business logic, no crypto."""


def calculate_total_5033(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5033():
    return 'module 5033 handles orders and invoices'
