"""Service module 2709: business logic, no crypto."""


def calculate_total_2709(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_2709():
    return 'module 2709 handles orders and invoices'
