"""Service module 41438: business logic, no crypto."""


def calculate_total_41438(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_41438():
    return 'module 41438 handles orders and invoices'
