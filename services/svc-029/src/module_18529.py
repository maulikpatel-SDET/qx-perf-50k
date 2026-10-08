"""Service module 18529: business logic, no crypto."""


def calculate_total_18529(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_18529():
    return 'module 18529 handles orders and invoices'
