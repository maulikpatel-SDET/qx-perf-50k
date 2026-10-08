"""Service module 45108: business logic, no crypto."""


def calculate_total_45108(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45108():
    return 'module 45108 handles orders and invoices'
