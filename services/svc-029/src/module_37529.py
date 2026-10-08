"""Service module 37529: business logic, no crypto."""


def calculate_total_37529(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_37529():
    return 'module 37529 handles orders and invoices'
