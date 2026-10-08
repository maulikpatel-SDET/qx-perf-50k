"""Service module 3108: business logic, no crypto."""


def calculate_total_3108(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_3108():
    return 'module 3108 handles orders and invoices'
